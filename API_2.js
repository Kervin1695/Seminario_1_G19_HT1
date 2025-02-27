const express = require('express');
const app = express();

app.get("/check", (req, res) => {
    console.log("endpoint check");
    res.status(200).json({ message: "OK" });
});

app.get("/info", (req, res) => {
    console.log("endpoint info");
    res.json({
        Instancia: "Maquina 2 - Api 2",
        Curso: "Seminario de Sistemas 1 A",
        Grupo: "Grupo #19"
    });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});