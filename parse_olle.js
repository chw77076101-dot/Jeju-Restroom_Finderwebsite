const fs = require('fs');
const path = require('path');

const dataDir = path.join(__dirname, '제주올레길 Movescount GPS Map');
const outputFile = path.join(__dirname, 'jeju_olle_data.js');

// Helper to extract lat/lon from GPX content using Regex
function parseGpx(content) {
    const points = [];
    // Match <rtept lat="..." lon="..."> OR <trkpt lat="..." lon="...">
    const regex = /<(?:rtept|trkpt)\s+lat="([\d.]+)"\s+lon="([\d.]+)"/g;
    let match;
    while ((match = regex.exec(content)) !== null) {
        points.push({
            lat: parseFloat(match[1]),
            lng: parseFloat(match[2])
        });
    }
    return points;
}

// Helper to get course ID from filename
function getCourseId(filename) {
    // Examples: jeju_ollegil_01.gpx, jeju-ollegil_10-1.gpx, jeju_ollegil_18-1.gpx
    // Remove extension
    const name = filename.replace(/\.(gpx|kml)$/i, '');

    // Match patterns like "01", "10-1", "3A", "14-1", "1-1"
    // We look for a number followed optionally by -X or just X (letters) at the name's end
    // But be careful not to match the whole filename if it's just numbers.
    // Let's try matching the numeric part and optional suffix at the end of string.
    const match = name.match(/(\d{1,2}(?:[-_]?[a-zA-Z0-9]+)?)$/);
    if (match) {
        let id = match[1].replace('_', '-');
        // Remove leading zero if present (01 -> 1, 03A -> 3A)
        if (id.startsWith('0') && id.length > 1 && id[1] !== '-') {
            id = id.substring(1);
        }
        return id;
    }
    return null;
}

const OLLE_COLORS = {
    blue: "#0054FF",
    orange: "#FF7F00"
};

const courses = {};

try {
    const files = fs.readdirSync(dataDir);

    files.forEach(file => {
        if (!file.endsWith('.gpx')) return;

        const courseId = getCourseId(file);
        if (!courseId) {
            console.log(`Skipping file (no ID found): ${file}`);
            return;
        }

        // User requested to exclude Chuja-do (18-1)
        if (courseId === '18-1') {
            console.log(`Skipping Chuja-do (18-1) as requested`);
            return;
        }

        console.log(`Processing Course ${courseId} from ${file}...`);

        const content = fs.readFileSync(path.join(dataDir, file), 'utf8');
        const pathData = parseGpx(content);

        if (pathData.length > 0) {
            courses[courseId] = {
                name: `Olle Route ${courseId}`,
                // Alternate colors based on even/odd or just fixed logic (Olle trails usually use blue and orange ribbons)
                color: (parseInt(courseId) % 2 !== 0) ? OLLE_COLORS.blue : OLLE_COLORS.orange,
                path: pathData
            };
        } else {
            console.warn(`No points found for ${file}`);
        }
    });

    // Write to file
    const fileContent = `// Jeju Olle Trail Data - Generated from GPX
window.OLLE_COURSES = ${JSON.stringify(courses, null, 2)};
`;

    fs.writeFileSync(outputFile, fileContent);
    console.log(`Successfully generated jeju_olle_data.js with ${Object.keys(courses).length} courses.`);

} catch (err) {
    console.error("Error processing GPX files:", err);
}
