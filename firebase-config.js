// ============================================================
//  PASTE YOUR FIREBASE CREDENTIALS HERE
//  Get these from: Firebase Console → Project Settings → Your Apps
// ============================================================

const firebaseConfig = {
  apiKey: "AIzaSyBqfCg-dogZWIcWaQIzEJOSEsgd5x_s__g",
  authDomain: "sri-sai-chess-academy.firebaseapp.com",
  projectId: "sri-sai-chess-academy",
  storageBucket: "sri-sai-chess-academy.firebasestorage.app",
  messagingSenderId: "1093972011225",
  appId: "1:1093972011225:web:577f1ab01c75b082b936c8"
};

// Local Dashboard credentials (instead of storing in code, consider fetching from a secure backend or database in production)
const ADMIN_USERNAME = "admin";
const ADMIN_PASSWORD = "password123";

export { firebaseConfig, ADMIN_USERNAME, ADMIN_PASSWORD };
