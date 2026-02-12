// Jeju Olle Trail Mock Data (Approximate Paths)
// Real data would require GPX files or Kakao Map Trekking API

const OLLE_COURSES = {
    "1": {
        name: "Olle Route 1 (Siheung - Gwangchigi)",
        color: "#0054FF", // Olle Blue
        path: [
            { lat: 33.4777, lng: 126.9067 }, // Siheung Elementary School (Start)
            { lat: 33.4720, lng: 126.9150 }, // Malmi Oreum
            { lat: 33.4650, lng: 126.9200 },
            { lat: 33.4600, lng: 126.9300 },
            { lat: 33.4580, lng: 126.9350 }, // Al Oreum
            { lat: 33.4500, lng: 126.9400 },
            { lat: 33.4400, lng: 126.9300 }, // Seongsan
            { lat: 33.4500, lng: 126.9200 }, // Gwangchigi Beach (End)
        ]
    },
    "6": {
        name: "Olle Route 6 (Soesokkak - Olle Tourist Center)",
        color: "#FF8A00", // Olle Orange
        path: [
            { lat: 33.2500, lng: 126.6230 }, // Soesokkak
            { lat: 33.2480, lng: 126.6100 },
            { lat: 33.2450, lng: 126.5900 }, // Bomok
            { lat: 33.2420, lng: 126.5800 },
            { lat: 33.2400, lng: 126.5700 }, // Sojongbang Falls
            { lat: 33.2460, lng: 126.5600 }, // Seogwipo Port
            { lat: 33.2480, lng: 126.5580 }, // Olle Tourist Center
        ]
    },
    "7": {
        name: "Olle Route 7 (Olle Tourist Center - Wolpyeong)",
        color: "#0054FF",
        path: [
            { lat: 33.2480, lng: 126.5580 }, // Start
            { lat: 33.2500, lng: 126.5500 }, // Oedolgae
            { lat: 33.2400, lng: 126.5400 },
            { lat: 33.2350, lng: 126.5200 }, // Beophwan Port
            { lat: 33.2300, lng: 126.5000 },
            { lat: 33.2350, lng: 126.4800 }, // Gangjeong
            { lat: 33.2400, lng: 126.4600 }, // Wolpyeong
        ]
    }
};

window.OLLE_COURSES = OLLE_COURSES;
