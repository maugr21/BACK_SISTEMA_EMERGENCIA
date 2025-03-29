// Importar Firebase y Realtime Database
import { initializeApp } from "firebase/app";
import { getDatabase, ref, get, child, set } from "firebase/database";

// Configuración de Firebase (usa tu configuración)
const firebaseConfig = {
  apiKey: "AIzaSyDITT8YDclV-CFOl7WbfWd9xLjGjkgYzt0",
  authDomain: "hackathon25-7950d.firebaseapp.com",
  databaseURL: "https://hackathon25-7950d-default-rtdb.firebaseio.com",
  projectId: "hackathon25-7950d",
  storageBucket: "hackathon25-7950d.appspot.com",
  messagingSenderId: "75295474529",
  appId: "1:75295474529:web:d554aa6f077024845f3b20",
  measurementId: "G-5P7PCMD7EB"
};

// Inicializar Firebase
const app = initializeApp(firebaseConfig);
const db = getDatabase(app);

// Exportar la base de datos para usarla en otros archivos
export { db };

// 🔹 Función para escribir datos en Firebase
function writeUserData(idReporte, desc) {
  set(ref(db, "Reporte/" + idReporte), {
    description: desc
  })
    .then(() => {
      console.log("Reporte agregado correctamente");
    })
    .catch((error) => {
      console.error("Error al escribir en la base de datos:", error);
    });
}


writeUserData("R00006", "Incendio en casa habitación");

// 🔹 Función para leer datos desde Firebase
function readUserData(idReporte) {
  const dbRef = ref(db);
  get(child(dbRef, `Reporte/${idReporte}`))
    .then((snapshot) => {
      if (snapshot.exists()) {
        console.log("Datos del reporte:", snapshot.val());
      } else {
        console.log("No hay datos disponibles");
      }
    })
    .catch((error) => {
      console.error("Error al leer datos:", error);
    });
}

readUserData("R00001");

function initMap() {
  const center = { lat: 20.5888, lng: -100.3899 }; 
  const map = new google.maps.Map(document.getElementById("map"), {
    center: center,
    zoom: 10
  });
}
