# aiG
Free AI Image Editor, Instant Photo Editing Without Prompts.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Status](https://img.shields.io/badge/Status-MVP-brightgreen)
![Version](https://img.shields.io/badge/Version-0.1.0-blue)

**Edit photos instantly with AI. No prompts. No learning curve. Just click and download.**

Transform your images with professional AI editing in seconds. Choose from pre-designed editing templates, upload your photo, and get instant results. Perfect for content creators, marketers, photographers, and anyone who wants beautiful edited images without the complexity.

---

## What is aiG ?

aiG is a **free, open-source AI-powered image editor** that removes the friction from AI photo editing. Instead of writing complex prompts, users simply:

1. **Browse** visual editing templates (Vintage, Vibrant, B&W, etc.)
2. **Click** the style they want
3. **Upload** their image
4. **Download** the AI-edited result

Built with **Google's Gemini Nano API**, aiG delivers professional-quality edits instantly,perfect for:
-  **Content Creators** - Quick Instagram/TikTok content
-  **Photographers** - Quick touches without desktop software
-  **Casual Users** - Beautiful edits, no technical knowledge

---

##  Features

### Core Features (MVP)
-  **5+ AI Editing Templates** - Vibrant, Vintage, B&W, Moody, Soft Focus, and more
-  **Prompt-Free Editing** - No need to write technical prompts
-  **One-Click Processing** - Select template → Upload → Download
-  **Instant Results** - Powered by Gemini Nano for fast processing
-  **Multiple Format Support** - JPEG, PNG, WebP
-  **Responsive Design** - Works on desktop, tablet, mobile
-  **Free & Open Source** - MIT License, no account required

### Planned Features (v2+)
- User accounts & image history
- Custom template creation
- Batch processing (edit multiple images)
- Advanced settings (intensity, blending)
- Community template sharing
- Mobile app (iOS/Android)
- API for developers

---

##  Quick Start

### Live Demo
 **[Try aiG Now](https://aiG.app)** (demo link when deployed)

### Local Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/aiG.git
cd aiG

# Install dependencies (both frontend & backend)
npm install

# Configure environment variables
cp packages/backend/.env.example packages/backend/.env
cp packages/frontend/.env.example packages/frontend/.env

# Add your Gemini API key to packages/backend/.env
# GEMINI_API_KEY=your_api_key_here

# Start both services simultaneously
npm run dev
```

**That's it!** 
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

---

## Tech Stack

### Frontend
- **React 18** - Modern UI library
- **Vite** - Lightning-fast build tool
- **Tailwind CSS** - Utility-first styling

### Backend
- **Python + Django** - Fast, scalable API
- **Google Gemini Nano API** - AI image editing engine
- **CORS** - Cross-origin resource sharing


##  How It Works

### User Flow

```
1. User visits aiG
2. Browsing gallery of AI editing templates
3. Selects desired editing style (e.g., "Vintage Film")
4. Uploads their image (JPEG, PNG, WebP)
5. AI processes image with template's preset prompt
6. Edited image displays in browser
7. User downloads the result
8. Optional: Edit another image
```


## Contributing

We love contributions! Whether you're fixing bugs, adding features, or improving documentation, your help is welcome.

### For Contributors

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/amazing-feature`
3. **Commit changes:** `git commit -m '[SCOPE] Description'`
4. **Push to branch:** `git push origin feature/amazing-feature`
5. **Open a Pull Request**

---

---

## Security & Privacy

- **No Account Required** - Edit without registration
- **No Data Storage** - Images deleted after download
- **HTTPS Only** - Secure connections
- **API Key Protection** - Keys never exposed to client
- **Open Source** - Code auditable by community

---

## Performance Optimizations

- Image compression before processing
- Lazy loading for gallery
- Rate limiting to prevent abuse

---



## Supported Image Formats

**Input Formats:**
- JPEG (.jpg, .jpeg)
- PNG (.png)

**Output Formats:**
- JPEG 
- PNG

**File Size Limits:**
- Maximum: 10MB
- Recommended: < 5MB for faster processing

---

## System Requirements

### Browser Support
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari 12+, Chrome Android)

---


##  Known Issues & Limitations

### Current (MVP)
- Editing is synchronous (user must wait)
- No image history or storage
- Limited to 8 templates
- No custom prompts (intentional for MVP)

### Planned Fixes (v2)
- Async processing with background jobs
- User accounts with image history
- Unlimited custom templates
- Advanced prompt editor

---

##  FAQ

### Q: Is aiG free?
**A:** Yes! aiG is completely free and open source (MIT License).

### Q: Do I need an account?
**A:** No account required. Just upload and edit.

### Q: Are my images stored?
**A:** No. Images are deleted after download. We don't store anything.

### Q: Can I use aiG offline?
**A:** Not yet, Currently requires internet connection.

### Q: Is there an API for developers?
**A:** API is planned for v2. Star the repo to be notified of updates.

### Q: Can I contribute?
**A:** Absolutely!

### Q: How does it compare to [Photoshop/Canva/etc]?
**A:** aiG is for quick, AI-powered edits without learning curves. It's complementary to professional tools, not a replacement.

---

## Why aiG?

| Feature | aiG | Competitors |
|---------|----------|-------------|
| **No Prompts** | ✅ Yes | ❌ No |
| **Free** | ✅ Yes | ❌ Often paid |
| **No Account** | ✅ Yes | ❌ Usually required |
| **Open Source** | ✅ Yes | ❌ Proprietary |
| **One-Click Editing** | ✅ Yes | ❌ Complex UI |
| **No Learning Curve** | ✅ Yes | ❌ Steep learning |

---

---

## License

aiG is open source software licensed under the [MIT License](LICENSE). You're free to use, modify, and distribute it.

---

## Acknowledgments

- **Google Gemini API** - AI image editing engine
- **React Community** - Frontend framework
- **Express.js** - Backend framework
- **Our Contributors** - Making this project better every day

---

##  Team

- **[Developer 1]** - Backend Lead
- **[Developer 2]** - Frontend Lead
- **[Developer 3]** - Backend

- 
- Image enhancement, photo enhancement AI
- Free online photo editor, web-based image editor
- Social media content creation, quick photo editing
