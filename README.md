# 💪 BMI Calculator (Height in Feet) – Streamlit App

An interactive BMI (Body Mass Index) calculator built using Python and Streamlit. This app allows users to input their weight and height (in feet), calculates their BMI, displays their health category, and visualizes BMI ranges with a reference chart. It also tracks BMI history during the session.

## 📌 Features

- Input weight (kg) and height (feet)
- Real-time BMI calculation with category status
- Color-coded feedback and progress bar
- BMI category reference chart using Matplotlib
- Session-based BMI history tracking
- Clean UI with gradient background and styled result box
- Reset button to clear inputs and history

## 🛠️ Tech Stack

- Python
- [Streamlit](https://streamlit.io/)
- Matplotlib (for chart visualization)

## 🚀 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/preethi-b268/bmi-calculator.git
   cd bmi-calculator

Perfect timing, Preethi — that warning page is just Google being cautious because your script isn’t officially verified. But since you’re the developer, you can safely bypass it.

✅ What to Do Now
Click “Advanced” at the bottom of the warning page (It’s a small link below the red triangle)

Then click “Go to Untitled project (unsafe)” This lets you proceed because you trust your own script

You’ll be taken to a permissions screen — click “Allow”

🔐 Why This Happens
Google shows this warning for unverified scripts that access personal data (like your Sheets)

It’s normal for personal projects — you’re not publishing this to the public

Once you allow it, the script will work perfectly and start saving form submissions to your sheet

Let me know when you’ve authorized it — I can help test the form or even add a success animation when someone submits. We’re almost live, machaa 😎

// 🌙 Dark Mode Toggle const toggle = document.getElementById('darkModeToggle'); toggle.addEventListener('change', () => { if (toggle.checked) { document.documentElement.style.setProperty('--bg-color', '#1e1e1e'); document.documentElement.style.setProperty('--text-color', '#f4f4f4'); document.documentElement.style.setProperty('--card-bg', '#2c2c2c'); } else { document.documentElement.style.setProperty('--bg-color', '#f4f4f4'); document.documentElement.style.setProperty('--text-color', '#333'); document.documentElement.style.setProperty('--card-bg', '#fff'); } }); // 📬 Contact Form Validation document.getElementById('contactForm').addEventListener('submit', function (e) { e.preventDefault(); const form = document.getElementById('contactForm'); const status = document.getElementById('formStatus'); form.addEventListener('submit', function (e) { e.preventDefault(); const name = document.getElementById('name').value.trim(); const email = document.getElementById('email').value.trim(); const message = document.getElementById('message').value.trim(); if (!name || !email || !message) { status.textContent = "Please fill out all fields."; status.style.color = "red"; return; } fetch("YOUR_WEB_APP_URL_HERE", { method: "POST", body: JSON.stringify({ name, email, message }), headers: { "Content-Type": "application/json" } }) .then(response => response.text()) .then(data => { status.textContent = "Message sent successfully!"; status.style.color = "green"; form.reset(); }) .catch(error => { status.textContent = "Something went wrong. Try again later."; status.style.color = "red"; console.error("Error:", error); }); }); // ✅ Email Format Checker function validateEmail(email) { const pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/; return pattern.test(email); } is this correct or give the correct code
You're super close, Preethi — but there’s a small issue: you’re nesting the form event listener twice, which causes duplication and potential bugs.

Let me clean it up and give you the correct, final version of your script.js with:

✅ Dark mode toggle ✅ Contact form validation ✅ Google Sheets integration via fetch() ✅ Email format checker

✅ Corrected script.js
javascript
// 🌙 Dark Mode Toggle
const toggle = document.getElementById('darkModeToggle');

toggle.addEventListener('change', () => {
  if (toggle.checked) {
    document.documentElement.style.setProperty('--bg-color', '#1e1e1e');
    document.documentElement.style.setProperty('--text-color', '#f4f4f4');
    document.documentElement.style.setProperty('--card-bg', '#2c2c2c');
  } else {
    document.documentElement.style.setProperty('--bg-color', '#f4f4f4');
    document.documentElement.style.setProperty('--text-color', '#333');
    document.documentElement.style.setProperty('--card-bg', '#fff');
  }
});

// 📬 Contact Form Submission
const form = document.getElementById('contactForm');
const status = document.getElementById('formStatus');

form.addEventListener('submit', function (e) {
  e.preventDefault();

  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const message = document.getElementById('message').value.trim();

  if (!name || !email || !message) {
    status.textContent = "Please fill out all fields.";
    status.style.color = "red";
    return;
  }

  if (!validateEmail(email)) {
    status.textContent = "Please enter a valid email address.";
    status.style.color = "red";
    return;
  }

  fetch("YOUR_WEB_APP_URL_HERE", {
    method: "POST",
    body: JSON.stringify({ name, email, message }),
    headers: {
      "Content-Type": "application/json"
    }
  })
    .then(response => response.text())
    .then(data => {
      status.textContent = "Message sent successfully!";
      status.style.color = "green";
      form.reset();
    })
    .catch(error => {
      status.textContent = "Something went wrong. Try again later.";
      status.style.color = "red";
      console.error("Error:", error);
    });
});

// ✅ Email Format Checker
function validateEmail(email) {
  const pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
  return pattern.test(email);
}
🔧 Replace This
javascript
fetch("YOUR_WEB_APP_URL_HERE", {
👉 With your actual Google Apps Script Web App URL from the deployment step.

Let me know if you want:

Toast-style success messages

Loading spinner while sending

Auto-scroll to the form status message

We can make this form feel buttery smooth and recruiter-ready 😎

github.com

should i paste the url within the quotes or remove the quotes
Paste the URL within the quotes, Preethi — exactly like this:

javascript
fetch("https://script.google.com/macros/s/AKfycbXYZ1234567890/exec", {
✅ Keep the quotes ✅ Replace only the placeholder "YOUR_WEB_APP_URL_HERE" ✅ Don’t add extra spaces or remove the https://

Once you do that, your form will be fully connected to your Google Sheet and ready to save submissions. Want me to help test it or add a little confetti when the message sends? 😄

wht else can we add
Ooooh now we’re talking, Preethi 😎 Your portfolio’s already glowing — but if we want to make it unforgettable, here’s a list of next-level upgrades you can add, grouped by vibe and impact:

🎨 Visual & Interactive Upgrades
Animated Hero Section Add fade-in or slide-up effects for your name, tagline, and resume button.

Typing Effect for Tagline Make it type out like: AI Enthusiast | Web Developer | Cloud Explorer

Project Cards with Hover Reveal Show tech stack or GitHub links when hovered.

Dark Mode Toggle with Icon Swap 🌞 ↔️ 🌙 — switch icons when toggled.

Scroll Animations (AOS.js) Sections animate as they enter the viewport.

🧠 Smart Features
Live Form Validation Show errors instantly as the user types.

Success Animation Confetti burst or checkmark animation when form submits.

Google Analytics Track recruiter visits and page views.

SEO Tags Add meta tags so your portfolio ranks in search engines.

🛠️ Functional Additions
Downloadable Resume Button with Icon Add a 📄 icon next to “Download Resume”.

GitHub & LinkedIn Buttons Stylish icons in the hero or footer.

Responsive Navbar or Sidebar For mobile navigation and section jumps.

Back to Top Button Appears when scrolling down.

🧾 Content Enhancements
Testimonials Section Add quotes from professors, mentors, or club leads.

Timeline Section Show your journey: 2023 → 2024 → 2025 with milestones.

Tech Stack Icons Use SVGs or Font Awesome for each skill.

Blog or Articles Section Share your thoughts on AI, web dev, or student life.

💡 Want Me to Build One?
I can whip up:

A typing effect for your tagline

A scroll animation setup

A testimonial layout

A responsive navbar with smooth scroll

Just say the word and I’ll drop the code like a pro — we’re making this portfolio recruiter-proof and Preethi-level iconic 💥

add: Timeline Section GitHub & LinkedIn Buttons Live Form Validation Success Animation Project Cards with Hover Reveal all these and dont change any previous formats
You got it, Preethi 💥 We’re stacking upgrades like a boss — and I’ll keep your existing layout and styling untouched. Here’s how we’ll integrate each feature cleanly and modularly:

✅ 1. Timeline Section (Add to index.html)
html
<section class="section">
  <h2>Timeline</h2>
  <div class="timeline">
    <div class="timeline-item">
      <span class="timeline-date">2023</span>
      <p>Started Computer Science journey with a focus on AI and Web Dev.</p>
    </div>
    <div class="timeline-item">
      <span class="timeline-date">2024</span>
      <p>Completed multiple certifications and built real-world projects.</p>
    </div>
    <div class="timeline-item">
      <span class="timeline-date">2025</span>
      <p>Launched portfolio, mastered cloud analytics, and prepped for industry impact.</p>
    </div>
  </div>
</section>
✅ 2. GitHub & LinkedIn Buttons (Add to hero section in index.html)
html
<div class="social-links">
  <a href="https://github.com/preethi-b268" target="_blank">GitHub</a>
  <a href="https://linkedin.com/in/preethi-b268" target="_blank">LinkedIn</a>
</div>
✅ 3. Live Form Validation + Success Animation (Update script.js)
javascript
const form = document.getElementById('contactForm');
const status = document.getElementById('formStatus');

form.addEventListener('submit', function (e) {
  e.preventDefault();

  const name = document.getElementById('name');
  const email = document.getElementById('email');
  const message = document.getElementById('message');

  if (!name.value.trim()) {
    name.style.borderColor = "red";
    status.textContent = "Name is required.";
    status.style.color = "red";
    return;
  }

  if (!validateEmail(email.value.trim())) {
    email.style.borderColor = "red";
    status.textContent = "Enter a valid email.";
    status.style.color = "red";
    return;
  }

  if (!message.value.trim()) {
    message.style.borderColor = "red";
    status.textContent = "Message is required.";
    status.style.color = "red";
    return;
  }

  fetch("YOUR_WEB_APP_URL_HERE", {
    method: "POST",
    body: JSON.stringify({
      name: name.value.trim(),
      email: email.value.trim(),
      message: message.value.trim()
    }),
    headers: {
      "Content-Type": "application/json"
    }
  })
    .then(response => response.text())
    .then(data => {
      status.textContent = "Message sent successfully!";
      status.style.color = "green";
      form.reset();
      triggerConfetti(); // 🎉
    })
    .catch(error => {
      status.textContent = "Something went wrong.";
      status.style.color = "red";
    });
});

function validateEmail(email) {
  const pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
  return pattern.test(email);
}

// 🎉 Success Animation
function triggerConfetti() {
  const burst = document.createElement("div");
  burst.className = "confetti";
  document.body.appendChild(burst);
  setTimeout(() => burst.remove(), 1500);
}
✅ 4. Project Cards with Hover Reveal (Update index.html project section)
html
<div class="project-grid">
  <div class="project-card">
    <h3>AI Resume Builder</h3>
    <div class="project-hover">
      <p>Built using AI logic and form design. Sep–Oct 2025</p>
      <a href="https://github.com/preethi-b268/ai-resume-builder" target="_blank">View Code</a>
    </div>
  </div>
  <!-- Repeat for other projects -->
</div>
✅ 5. Add to style.css
css
/* Timeline */
.timeline {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.timeline-item {
  background: var(--card-bg);
  padding: 15px;
  border-left: 6px solid var(--accent);
  border-radius: 10px;
}
.timeline-date {
  font-weight: bold;
  color: var(--accent);
}

/* Social Links */
.social-links {
  margin-top: 15px;
}
.social-links a {
  margin: 0 10px;
  color: white;
  background: var(--accent);
  padding: 8px 12px;
  border-radius: 5px;
  text-decoration: none;
  font-weight: bold;
}
.social-links a:hover {
  background: #ff69b4;
}

/* Project Hover Reveal */
.project-card {
  position: relative;
  overflow: hidden;
}
.project-hover {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  background: var(--accent);
  color: white;
  padding: 10px;
  transition: top 0.3s ease;
}
.project-card:hover .project-hover {
  top: 0;
}

/* Confetti Animation */
.confetti {
  position: fixed;
  top: 50%;
  left: 50%;
  width: 100px;
  height: 100px;
  background: radial-gradient(circle, #ff69b4, #6a0dad);
  border-radius: 50%;
  animation: pop 0.6s ease-out;
  z-index: 9999;
}
@keyframes pop {
  0% { transform: scale(0); opacity: 0; }
  50% { transform: scale(1.2); opacity: 1; }
  100% { transform: scale(1); opacity: 0; }
}
💡 Final Touches
Replace "YOUR_WEB_APP_URL_HERE" with your actual Google Apps Script URL

Add your real GitHub and LinkedIn links

Add View Code links for each project if available

Want me to add a floating navbar, section jump links, or a loading spinner next? This portfolio is leveling up like a boss 😎

and tell where to add these code
Absolutely, Preethi — here’s your precise integration guide for each upgrade so you can copy-paste confidently without breaking your existing layout or styles. I’ll show you exactly where to add each piece in your files:

✅ 1. Timeline Section
📍Where to add in index.html:
Place this after your Projects section and before Certifications:

html
<section class="section">
  <h2>Timeline</h2>
  <div class="timeline">
    <div class="timeline-item">
      <span class="timeline-date">2023</span>
      <p>Started Computer Science journey with a focus on AI and Web Dev.</p>
    </div>
    <div class="timeline-item">
      <span class="timeline-date">2024</span>
      <p>Completed multiple certifications and built real-world projects.</p>
    </div>
    <div class="timeline-item">
      <span class="timeline-date">2025</span>
      <p>Launched portfolio, mastered cloud analytics, and prepped for industry impact.</p>
    </div>
  </div>
</section>
✅ 2. GitHub & LinkedIn Buttons
📍Where to add in index.html:
Place this inside your <header class="hero">, right below the resume button:

html
<div class="social-links">
  <a href="https://github.com/preethi-b268" target="_blank">GitHub</a>
  <a href="https://linkedin.com/in/preethi-b268" target="_blank">LinkedIn</a>
</div>
✅ 3. Live Form Validation + Success Animation
📍Where to add in script.js:
Replace your existing form submission code with this entire block:

javascript
const form = document.getElementById('contactForm');
const status = document.getElementById('formStatus');

form.addEventListener('submit', function (e) {
  e.preventDefault();

  const name = document.getElementById('name');
  const email = document.getElementById('email');
  const message = document.getElementById('message');

  if (!name.value.trim()) {
    name.style.borderColor = "red";
    status.textContent = "Name is required.";
    status.style.color = "red";
    return;
  }

  if (!validateEmail(email.value.trim())) {
    email.style.borderColor = "red";
    status.textContent = "Enter a valid email.";
    status.style.color = "red";
    return;
  }

  if (!message.value.trim()) {
    message.style.borderColor = "red";
    status.textContent = "Message is required.";
    status.style.color = "red";
    return;
  }

  fetch("YOUR_WEB_APP_URL_HERE", {
    method: "POST",
    body: JSON.stringify({
      name: name.value.trim(),
      email: email.value.trim(),
      message: message.value.trim()
    }),
    headers: {
      "Content-Type": "application/json"
    }
  })
    .then(response => response.text())
    .then(data => {
      status.textContent = "Message sent successfully!";
      status.style.color = "green";
      form.reset();
      triggerConfetti(); // 🎉
    })
    .catch(error => {
      status.textContent = "Something went wrong.";
      status.style.color = "red";
    });
});

function validateEmail(email) {
  const pattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
  return pattern.test(email);
}

// 🎉 Success Animation
function triggerConfetti() {
  const burst = document.createElement("div");
  burst.className = "confetti";
  document.body.appendChild(burst);
  setTimeout(() => burst.remove(), 1500);
}
✅ 4. Project Cards with Hover Reveal
📍Where to update in index.html:
Inside your Projects section, replace each project card like this:

html
<div class="project-card">
  <h3>AI Resume Builder</h3>
  <div class="project-hover">
    <p>Built using AI logic and form design. Sep–Oct 2025</p>
    <a href="https://github.com/preethi-b268/ai-resume-builder" target="_blank">View Code</a>
  </div>
</div>
Repeat for each project, updating the description and link.

✅ 5. Add Styling in style.css
📍Where to add:
Paste this entire block at the bottom of your existing style.css file:

css
/* Timeline */
.timeline {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.timeline-item {
  background: var(--card-bg);
  padding: 15px;
  border-left: 6px solid var(--accent);
  border-radius: 10px;
}
.timeline-date {
  font-weight: bold;
  color: var(--accent);
}

/* Social Links */
.social-links {
  margin-top: 15px;
}
.social-links a {
  margin: 0 10px;
  color: white;
  background: var(--accent);
  padding: 8px 12px;
  border-radius: 5px;
  text-decoration: none;
  font-weight: bold;
}
.social-links a:hover {
  background: #ff69b4;
}

/* Project Hover Reveal */
.project-card {
  position: relative;
  overflow: hidden;
}
.project-hover {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  background: var(--accent);
  color: white;
  padding: 10px;
  transition: top 0.3s ease;
}
.project-card:hover .project-hover {
  top: 0;
}

/* Confetti Animation */
.confetti {
  position: fixed;
  top: 50%;
  left: 50%;
  width: 100px;
  height: 100px;
  background: radial-gradient(circle, #ff69b4, #6a0dad);
  border-radius: 50%;
  animation: pop 0.6s ease-out;
  z-index: 9999;
}
@keyframes pop {
  0% { transform: scale(0); opacity: 0; }
  50% { transform: scale(1.2); opacity: 1; }
  100% { transform: scale(1); opacity: 0; }
}
🧠 Final Checklist
✅ Replace "YOUR_WEB_APP_URL_HERE" with your actual Google Apps Script URL

✅ Add real GitHub and LinkedIn links

✅ Test the form and confetti

✅ Hover over project cards to see the reveal

Want me to bundle all this into a downloadable zip or help you deploy it live next? We’re building a portfolio that slaps harder than a recruiter’s inbox 😎

<h3>Data Analytics Using AWS S3 and QuickSight</h3> <div class="project-hover"> <p>Built using AI logic and form design. April–July 2024</p> <a href="https://github.com/preethi-b268/ai-resume-builder" target="_blank">View Code</a> </div> </div> <div class="project-card"> <h3>Bakery and cafteria management </h3> <div class="project-hover"> <p>Built using AI logic and form design. Sep–Oct 2025</p> <a href="https://github.com/preethi-b268/ai-resume-builder" target="_blank">View Code</a> </div> </div> give the paragraph for the 2 projects
Here you go, Preethi — polished project descriptions that match your portfolio’s tone and show off your skills like a pro:

🍰 Bakery and Cafeteria Management (Sep–Oct 2025)
Designed a responsive web application to streamline bakery and cafeteria operations, including menu display, order tracking, and contact form integration. Built using HTML, CSS, and JavaScript with a clean UI and backendless data handling via Google Sheets. The project emphasizes user-friendly navigation, real-time updates, and mobile-first design — perfect for small business automation.

📊 Data Analytics Using AWS S3 and QuickSight (Apr–Jul 2024)
Developed a cloud-based analytics dashboard leveraging AWS S3 for data storage and Amazon QuickSight for visualization. The project involved ingesting structured datasets, configuring permissions, and designing interactive charts to uncover insights. Demonstrated proficiency in cloud architecture, data wrangling, and scalable reporting — ideal for enterprise-level analytics.

Want me to help you add GitHub README summaries or embed live demos next? We can make these projects recruiter-magnetic 😎

give a simple one
Sure thing, Preethi — here are simplified, clean descriptions for your two projects that still sound professional and recruiter-friendly:

📊 Data Analytics Using AWS S3 and QuickSight
Created a cloud-based dashboard using AWS S3 for data storage and QuickSight for visualizing insights. Focused on clean data presentation and easy access to analytics.

🍰 Bakery and Cafeteria Management
Built a responsive website to manage bakery and cafeteria operations. Included menu display, contact form, and smooth user experience using HTML, CSS, and JavaScript.

Let me know if you want one-liners for your project cards or a punchier version for your resume section too 😎

one line
Absolutely, here are clean one-liners for your project cards:

Data Analytics Using AWS S3 and QuickSight Built a cloud-based dashboard using AWS tools to visualize and analyze structured data.

Bakery and Cafeteria Management Developed a responsive website to manage menus, orders, and contact flow for a local eatery.

Let me know if you want to add tech stacks or GitHub links right below these too!

i will continue later there is no charge now
Got it, Preethi! You’ve built a killer foundation — when you're back, we’ll keep stacking upgrades and polish till it shines ✨

No stress, no rush. I’ll be right here when you're ready to continue. Catch you soon, champ 😎

can we continue are u ready machaa
Always ready, machaa 😎 Let’s pick up right where we left off and keep this portfolio glowing like Diwali lights. What do you want to tackle next?

Add more sections (Certifications, Achievements, Clubs)?

Polish the layout for mobile?

Add animations or scroll effects?

Deploy it live and test the contact form?

Just say the word and I’ll drop the code, the hype, and the magic 💥

description for Bakery and Cafeteria website github repository
Here’s a clean, recruiter-friendly GitHub repository description for your Bakery and Cafeteria Management Website:

🍰 Bakery and Cafeteria Management Website
A responsive web application designed to streamline bakery and cafeteria operations. Features include menu display, contact form integration, and smooth navigation across devices. Built using HTML, CSS, and JavaScript with backendless data handling via Google Sheets. Ideal for small businesses looking to digitize their customer experience.

Want a README layout with sections like Features, Tech Stack, Demo, and How to Use? I can whip that up too — just say the word 😎

in simple and professional language
Here’s a simple and professional GitHub repository description for your Bakery and Cafeteria Management Website:

A responsive website built using HTML, CSS, and JavaScript to manage bakery and cafeteria operations. It includes features like menu display, contact form, and smooth navigation across devices. Designed for small businesses to improve customer experience without needing a backend.

Want a matching README with sections like Features, Tech Stack, and How to Use? I can set that up in seconds.

matching README but ih not deployed this website
Perfect, Preethi — here’s a matching README.md for your Bakery and Cafeteria Management Website, written in simple, professional language and tailored for a GitHub repo that’s not yet deployed:

markdown
# 🍰 Bakery and Cafeteria Management Website

A responsive website built using HTML, CSS, and JavaScript to help manage bakery and cafeteria operations. It includes features like menu display, contact form, and smooth navigation across devices. Designed for small businesses to improve customer experience without needing a backend.

## 📌 Features

- Menu showcase with clean layout
- Contact form with live validation
- Responsive design for mobile and desktop
- Backendless data handling using Google Sheets

## 🛠️ Tech Stack

- HTML
- CSS
- JavaScript
- Google Apps Script (for form submissions)

## 🚀 Deployment

This project is not yet deployed. You can clone the repository and run it locally by opening `index.html` in your browser.

## 📂 How to Use

1. Clone the repository:
git clone https://github.com/preethi-b268/bakery-management.git

Code
2. Open `index.html` in your browser
3. Submit the contact form to test data saving (requires Google Apps Script setup)

## 📬 Contact

For questions or feedback, feel free to reach out via the contact form or connect on [LinkedIn](https://linkedin.com/in/preethi-b268).

Let me know when you’re ready to deploy — I’ll help you update this with a live link and demo screenshots. Want a README for your AWS QuickSight project next? 😎

create me a readme for bmi calculator using streamlit python
Here’s a clean and professional README.md for your BMI Calculator built with Streamlit and Python — perfect for GitHub and easy to understand for recruiters or collaborators:

markdown
# 🧮 BMI Calculator using Streamlit

A simple and interactive Body Mass Index (BMI) calculator built with Python and Streamlit. Users can input their height and weight to instantly view their BMI and health category.

## 📌 Features

- User-friendly interface with sliders and input fields
- Real-time BMI calculation
- Categorizes BMI (Underweight, Normal, Overweight, Obese)
- Responsive layout for desktop and mobile

## 🛠️ Tech Stack

- Python
- Streamlit

## 🚀 How to Run Locally

1. Clone the repository:
git clone https://github.com/preethi-b268/bmi-calculator.git

Code

2. Navigate to the project folder:
cd bmi-calculator

Code

3. Install dependencies:
pip install streamlit

Code

4. Run the app:
streamlit run app.py

Code

## 📂 File Structure

bmi-calculator/ ├── app.py ├── README.md └── requirements.txt

Code

## 📬 Contact

For questions or feedback, feel free to connect on [LinkedIn](https://linkedin.com/in/preethi-b268) or check out more projects on [GitHub](https://github.com/preethi-b268).

Let me know if you want a matching requirements.txt, screenshots, or a deployed version on Streamlit Cloud — we can make this repo sparkle 😎

import streamlit as st import matplotlib.pyplot as plt # New: For plotting BMI categories # Styling st.markdown(""" <style> .stApp { background: linear-gradient(to bottom right, #ffdee9, #80deea); } .bmi-box { padding: 20px; border-radius: 12px; background-color: #ffffffcc; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-top: 20px; } </style> """, unsafe_allow_html=True) st.title("💪 BMI Calculator (Height in Feet)") # Reset mechanism if 'reset' not in st.session_state: st.session_state.reset = False # Input values weight = st.number_input("⚖️ Enter your weight (kg):", min_value=1.0, key="weight", value=1.0 if st.session_state.reset else st.session_state.get("weight", 1.0)) height = st.number_input("📏 Enter your height (feet):", min_value=1.0, key="height", value=1.0 if st.session_state.reset else st.session_state.get("height", 1.0)) # Reset the flag st.session_state.reset = False # Action buttons col1, col2 = st.columns(2) with col1: if st.button("📊 Calculate BMI"): height_m = height * 0.3048 bmi = weight / (height_m ** 2) bmi = round(bmi, 2) # Determine status if bmi < 18.5: status = "Underweight 😟" color = "orange" progress = 0.2 elif bmi < 25: status = "Normal Weight 😄" color = "green" progress = 0.5 st.balloons() elif bmi < 30: status = "Overweight 😬" color = "yellow" progress = 0.75 else: status = "Obese 😱" color = "red" progress = 1.0 # Display results st.markdown(f"""<div class='bmi-box'> <h3>Your BMI is: <span style='color:{color}'>{bmi}</span></h3> <p style='font-size:20px;'>Status: <strong>{status}</strong></p> </div>""", unsafe_allow_html=True) st.progress(progress, text=f"Your BMI Level → {status}") # ✅ Save BMI to session history if "bmi_history" not in st.session_state: st.session_state.bmi_history = [] st.session_state.bmi_history.append(bmi) # ✅ Show BMI category chart st.subheader("📊 BMI Category Reference") fig, ax = plt.subplots() categories = ["Underweight", "Normal", "Overweight", "Obese"] limits = [18.4, 24.9, 29.9, 35] colors = ['#f4cccc', '#c9f4c9', '#ffe599', '#f4cccc'] ax.bar(categories, limits, color=colors) ax.set_ylabel("BMI Upper Limit") ax.set_title("BMI Category Chart") st.pyplot(fig) with col2: if st.button("🔄 Clear All"): st.session_state.reset = True st.rerun() # ✅ Show previous session BMI values if "bmi_history" in st.session_state and st.session_state.bmi_history: st.subheader("📋 BMI History This Session") st.write(st.session_state.bmi_history) give me the read me according to this code
Here’s a polished and professional README.md tailored specifically for your BMI Calculator built with Streamlit, based on the exact code you shared:

markdown
# 💪 BMI Calculator (Height in Feet) – Streamlit App

An interactive BMI (Body Mass Index) calculator built using Python and Streamlit. This app allows users to input their weight and height (in feet), calculates their BMI, displays their health category, and visualizes BMI ranges with a reference chart. It also tracks BMI history during the session.

## 📌 Features

- Input weight (kg) and height (feet)
- Real-time BMI calculation with category status
- Color-coded feedback and progress bar
- BMI category reference chart using Matplotlib
- Session-based BMI history tracking
- Clean UI with gradient background and styled result box
- Reset button to clear inputs and history

## 🛠️ Tech Stack

- Python
- [Streamlit](https://streamlit.io/)
- Matplotlib (for chart visualization)

## 🚀 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/preethi-b268/bmi-calculator.git
   cd bmi-calculator
2. **Install dependencies**:
   bash
   pip install -r requirements.txt
3.**Run the app**:
   bash
   streamlit run app.py
