# Testing-web-TooGas
TOOGAS adalah aplikasi Software as a Service (SaaS) yang dirancang untuk memenuhi tugas proyek akhir mata kuliah Komputasi Awan. Aplikasi ini membantu pengguna mengelola tugas secara efektif dan efisien, mulai dari daftar pekerjaan sederhana hingga merencanakan proyek yang lebih besar.

Sebagai platform SaaS, TOOGAS menawarkan kemudahan aksesibilitas—pengguna dapat mengelola tugas dan catatan kapan pun dan di mana pun. Dengan antarmuka pengguna yang sederhana dan fitur-fitur praktis, aplikasi ini dirancang untuk menjaga pengguna tetap terorganisir dan produktif tanpa kerepotan.

✨ Fitur Utama
- 👤 Manajemen Akun Pengguna: Sistem autentikasi lengkap (Sign-up, Login, Reset Password) untuk mengamankan data pengguna.
- 📝 Provisioning Instans: Alokasi sumber daya secara dinamis untuk modul To-do List dan Notes bagi setiap pengguna.
- ⚖️ Penskalaan Instans (Kuota): Pengelolaan kuota dinamis yang dapat ditingkatkan sesuai kebutuhan pengguna.
- 💳 Sistem Billing: Model pembayaran pay-per-use yang transparan untuk penambahan kuota, dengan biaya harian untuk masa aktif paket.
- 🕒 Penjadwal Otomatis: Eksekusi tugas terjadwal (Cron Job) menggunakan Supabase Edge Functions untuk menonaktifkan paket kuota yang kedaluwarsa dan membersihkan data lama.
- 📜 Log Aktivitas: Pencatatan semua aktivitas penting pengguna untuk kemudahan audit dan pemantauan.
- 🛠️ Arsitektur & Teknologi
Proyek ini dibangun dengan arsitektur modern yang memisahkan antara frontend dan backend, memanfaatkan kekuatan Backend as a Service (BaaS) untuk efisiensi pengembangan.

1. Frontend
- Framework: Next.js (dengan App Router)
- Styling: Tailwind CSS dengan komponen siap pakai dari shadcn/ui
- State Management: Kombinasi useState, useEffect, dan useActionState dari React.
- Visualisasi Data: Recharts untuk menampilkan grafik dan data analitik.
- Deployment: Vercel
2. Backend as a Service (BaaS) & Database
- Platform: Supabase
- Database: PostgreSQL
- Auth: Supabase Auth untuk manajemen otentikasi.
- Serverless Functions: Supabase Edge Functions (Deno) untuk tugas terjadwal.
- API: Backend kustom menggunakan Express.js untuk menangani logika kompleks jika diperlukan.
