const express = require('express');
const cors = require('cors');
const fetch = require('node-fetch');

const app = express();
const port = 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Route: Ambil data booking dari backend Django
app.get('/api/bookings', async (req, res) => {
    try {
        const response = await fetch('http://localhost:8000/api/bookings/list/');
        if (!response.ok) {
            throw new Error('Gagal mengambil data dari Django');
        }

        const data = await response.json();
        res.json(data);
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Gagal mengambil data booking' });
    }
});

// Jalankan server
app.listen(port, () => {
    console.log(`Server berjalan di http://localhost:${port}`);
});
