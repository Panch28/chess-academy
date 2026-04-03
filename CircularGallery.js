import { Renderer, Camera, Transform, Plane, Orbit, Mesh, Program } from 'ogl';

const vertexShader = `
    attribute vec2 uv;
    attribute vec3 position;
    varying vec2 vUv;
    void main() {
        vUv = uv;
        gl_Position = vec4(position, 1.0);
    }
`;

const fragmentShader = `
    precision highp float;
    uniform sampler2D tMap;
    uniform float uAlpha;
    varying vec2 vUv;
    void main() {
        vec4 tex = texture2D(tMap, vUv);
        gl_FragColor = vec4(tex.rgb, tex.a * uAlpha);
    }
`;

export default class CircularGallery {
    constructor({
        element,
        items = [],
        bend = 3,
        textColor = '#ffffff',
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
        this.dragStart = 0;
        this.lastDrag = 0;
        
        this.init();
    }
    
    init() {
        this.renderer = new Renderer({ alpha: true, dpr: Math.min(window.devicePixelRatio, 2) });
        this.gl = this.renderer.gl;
        this.gl.canvas.style.cssText = `
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        `;
        this.element.appendChild(this.gl.canvas);
        
        this.camera = new Camera(this.gl, { fov: 45 });
        this.camera.position.set(0, 0, 6);
        
        this.scene = new Transform();
        
        this.resize();
        this.createGeometry();
        this.setupEvents();
        this.update();
    }
    
    createGeometry() {
        this.group = new Transform();
        this.planes = [];
        
        const spacing = 1.5;
        const count = this.items.length;
        
        for (let i = 0; i < count; i++) {
            const angle = (i / count) * Math.PI * 2;
            const x = Math.sin(angle) * this.bend;
            const z = Math.cos(angle) * this.bend - this.bend;
            
            const plane = new Mesh(this.gl, {
                geometry: new Plane(this.gl, {
                    width: 1.4,
                    height: 2,
                }),
                program: new Program(this.gl, {
                    vertex: vertexShader,
                    fragment: fragmentShader,
                    uniforms: {
                        tMap: { value: null },
                        uAlpha: { value: 1 }
                    },
                    transparent: true,
                }),
            });
            
            plane.position.x = x;
            plane.position.z = z;
            plane.rotation.y = -angle;
            
            const img = new Image();
            img.crossOrigin = 'anonymous';
            img.src = this.items[i];
            img.onload = () => {
                const texture = this.renderer.createTexture(img);
                plane.program.uniforms.tMap.value = texture;
            };
            
            this.planes.push(plane);
            this.group.addChild(plane);
        }
        
        this.scene.addChild(this.group);
    }
    
    setupEvents() {
        const onPointerDown = (e) => {
            this.isDragging = true;
            this.dragStart = e.clientX || e.touches?.[0]?.clientX || 0;
            this.lastDrag = this.dragStart;
        };
        
        const onPointerMove = (e) => {
            if (!this.isDragging) return;
            const current = e.clientX || e.touches?.[0]?.clientX || 0;
            const delta = (current - this.lastDrag) * 0.005;
            this.targetScroll -= delta * this.scrollSpeed;
            this.lastDrag = current;
        };
        
        const onPointerUp = () => {
            this.isDragging = false;
        };
        
        this.gl.canvas.addEventListener('mousedown', onPointerDown);
        this.gl.canvas.addEventListener('mousemove', onPointerMove);
        this.gl.canvas.addEventListener('mouseup', onPointerUp);
        this.gl.canvas.addEventListener('mouseleave', onPointerUp);
        this.gl.canvas.addEventListener('touchstart', onPointerDown, { passive: true });
        this.gl.canvas.addEventListener('touchmove', onPointerMove, { passive: true });
        this.gl.canvas.addEventListener('touchend', onPointerUp);
        
        window.addEventListener('resize', () => this.resize());
        
        // Mouse wheel scroll
        this.gl.canvas.addEventListener('wheel', (e) => {
            e.preventDefault();
            this.targetScroll += e.deltaY * 0.001 * this.scrollSpeed;
        }, { passive: false });
    }
    
    resize() {
        const rect = this.element.getBoundingClientRect();
        this.renderer.setSize(rect.width, rect.height);
        this.camera.perspective({ aspect: rect.width / rect.height });
    }
    
    update() {
        requestAnimationFrame(() => this.update());
        
        // Smooth scroll interpolation
        this.scroll += (this.targetScroll - this.scroll) * this.scrollEase;
        
        // Rotate group based on scroll
        this.group.rotation.y = this.scroll;
        
        // Update plane positions and opacity based on visibility
        this.planes.forEach((plane, i) => {
            const worldPos = new Transform();
            worldPos.position = plane.position;
            worldPos.parent = this.group;
            worldPos.updateMatrix();
            
            const z = worldPos.position.z;
            const dist = Math.abs(z + this.bend);
            
            // Fade based on distance
            plane.program.uniforms.uAlpha.value = Math.max(0, 1 - dist * 0.3);
        });
        
        this.renderer.render({ scene: this.scene, camera: this.camera });
    }
    
    destroy() {
        this.gl.canvas.remove();
    }
}
