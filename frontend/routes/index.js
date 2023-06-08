const express = require('express');
const router = express.Router();

// Admin route
router.get('/admin', (req, res) => {
  res.render('admin');
});

// Login route
router.get('/', (req, res) => {
    res.render('login');
  });

// Signup route
router.get('/signup', (req, res) => {
  res.render('signup');
});

// Login route
router.get('/login', (req, res) => {
  res.render('login');
});


// Form route
router.get('/form_update', (req, res) => {
  res.render('form_update');
});

// Form route
router.get('/form_add', (req, res) => {
  res.render('form_add');
});

// Form route
router.get('/form_show', (req, res) => {
  res.render('form_show');
});

// Dashboard route
router.get('/dashboard', (req, res) => {
  // Simulated book data
  const books = [
    { title: 'Book 1', desc: 'Description 1', price: 10.99 },
    { title: 'Book 2', desc: 'Description 2', price: 12.99 },
    // Additional books...
  ];

  res.render('dashboard', { books });
});

// Add new book route
router.post('/dashboard/add', (req, res) => {
  const { title, desc, price } = req.body;
  // Add book logic...

  // Redirect back to the dashboard
  res.redirect('/dashboard');
});

module.exports = router;
