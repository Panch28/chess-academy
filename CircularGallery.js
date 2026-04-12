import { Renderer, Camera, Transform, Plane, Mesh, Program, Texture } from 'ogl';

const vertex = /* glsl */`
    attribute vec3 position;
    attribute vec2 uv;
    uniform mat4 modelViewMatrix;
    uniform mat4 projectionMatrix;
    varying vec2 vUv;
    void main() {
        vUv = uv;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
`;

const fragment = /* glsl */`
    precision highp float;
    uniform sampler2D tMap;
    uniform float uAlpha;
    uniform float uGrayscale;
    varying vec2 vUv;
    void main() {
        vec4 tex = texture2D(tMap, vUv);
        float gray = dot(tex.rgb, vec3(0.299, 0.587, 0.114));
        vec3 color = mix(vec3(gray), tex.rgb, 1.0 - uGrayscale);
        gl_FragColor = vec4(color, tex.a * uAlpha);
    }
`;

export default class CircularGallery {
    constructor({
        element,
        items = [],
        bend = 3,
        textColor = '#d4af37',
        borderRadius = 0.05,
        scrollSpeed = 1,
        scrollEase = 0.05
    }) {
        this.element = element;
        this.items = items;
        this.bend = bend;
        this.textColor = textColor;
        this.borderRadius = borderRadius;
        this.scrollSpeed = scrollSpeed;
        this.scrollEase = scrollEase;

        this.scroll = 0;
        this.targetScroll = 0;
        this.isDragging = false;
        this.lastX = 0;
        this.rafId = null;
        this.planes = [];

        this.init();
    }

    get isMobile() {
        return window.innerWidth <= 768;
    }

    get cardWidth() {
        return this.isMobile ? 1.0 : 1.4;
    }

    get cardHeight() {
        return this.isMobile ? 1.6 : 2.0;
    }

    init() {
        this.renderer = new Renderer({
            alpha: true,
            antialias: true,
            dpr: Math.min(window.devicePixelRatio, 2)
        });
        this.gl = this.renderer.gl;

        Object.assign(this.gl.canvas.style, {
            position: 'absolute',
            top: '0',
            left: '0',
            width: '100%',
            height: '100%',
            touchAction: 'none'
        });

        this.element.appendChild(this.gl.canvas);

        this.camera = new Camera(this.gl, { fov: 45 });
        this.camera.position.z = this.isMobile ? 7 : 6;

        this.scene = new Transform();
        this.group = new Transform();
        this.group.setParent(this.scene);

        this.resize();
        this.buildPlanes();
        this.bindEvents();
        this.tick();
    }

    buildPlanes() {
        // Clear old planes
        this.planes.forEach(p => p.setParent(null));
        this.planes = [];

        const count = this.items.length;
        const radius = this.isMobile ? 2.5 : this.bend;

        for (let i = 0; i < count; i++) {
            const angle = (i / count) * Math.PI * 2;
            const x = Math.sin(angle) * radius;
            const z = Math.cos(angle) * radius - radius;

            const texture = new Texture(this.gl);

            const mesh = new Mesh(this.gl, {
                geometry: new Plane(this.gl, {
                    width: this.cardWidth,
                    height: this.cardHeight,
                }),
                program: new Program(this.gl, {
                    vertex,
                    fragment,
                    uniforms: {
                        tMap: { value: texture },
                        uAlpha: { value: 1.0 },
                        uGrayscale: { value: 0.8 }
                    },
                    transparent: true,
                    depthTest: false,
                }),
            });

            mesh.position.x = x;
            mesh.position.z = z;
            mesh.rotation.y = -angle;
            mesh.setParent(this.group);
            this.planes.push(mesh);

            // Load image
            const src = (this.items[i] && this.items[i].image) ? this.items[i].image : this.items[i];
            const img = new Image();
            img.crossOrigin = 'anonymous';
            img.src = src;
            img.onload = () => {
                texture.image = img;
                texture.needsUpdate = true;
            };
        }
    }

    bindEvents() {
        const canvas = this.gl.canvas;

        // Mouse
        canvas.addEventListener('mousedown', e => {
            this.isDragging = true;
            this.lastX = e.clientX;
        });
        window.addEventListener('mousemove', e => {
            if (!this.isDragging) return;
            const dx = e.clientX - this.lastX;
            this.targetScroll -= dx * 0.003 * this.scrollSpeed;
            this.lastX = e.clientX;
        });
        window.addEventListener('mouseup', () => { this.isDragging = false; });

        // Touch
        canvas.addEventListener('touchstart', e => {
            this.isDragging = true;
            this.lastX = e.touches[0].clientX;
        }, { passive: true });
        canvas.addEventListener('touchmove', e => {
            if (!this.isDragging) return;
            const dx = e.touches[0].clientX - this.lastX;
            this.targetScroll -= dx * 0.003 * this.scrollSpeed;
            this.lastX = e.touches[0].clientX;
        }, { passive: true });
        canvas.addEventListener('touchend', () => { this.isDragging = false; });

        

        // Resize debounced
        let resizeTimer;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(() => {
                this.resize();
                this.buildPlanes();
            }, 150);
        });
    }

    resize() {
        const w = this.element.clientWidth;
        const h = this.element.clientHeight;
        this.renderer.setSize(w, h);
        if (this.camera) {
            this.camera.perspective({ aspect: w / h });
            this.camera.position.z = this.isMobile ? 7 : 6;
        }
    }

    tick() {
        this.rafId = requestAnimationFrame(() => this.tick());

        this.scroll += (this.targetScroll - this.scroll) * this.scrollEase;
        this.group.rotation.y = this.scroll;

        const count = this.planes.length;
        this.planes.forEach((plane, i) => {
            const angle = (i / count) * Math.PI * 2;
            const effective = ((angle + this.scroll) % (Math.PI * 2) + Math.PI * 2) % (Math.PI * 2);
            const dist = Math.abs(effective - Math.PI);
            const normalized = dist / Math.PI; // 0 = front center, 1 = back

            plane.program.uniforms.uGrayscale.value = Math.min(1, normalized * 1.5);
            plane.program.uniforms.uAlpha.value = Math.max(0.1, 1 - normalized * 0.7);
        });

        this.renderer.render({ scene: this.scene, camera: this.camera });
    }

    destroy() {
        cancelAnimationFrame(this.rafId);
        this.gl.canvas.remove();
    }
}
