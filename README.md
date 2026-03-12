# Inik Kim — Quarto Personal Website

## Files

| File | Purpose |
|------|---------|
| `_quarto.yml` | Site config: title, navbar, theme |
| `index.qmd` | About / homepage |
| `publications.qmd` | Full publications list |
| `cv.qmd` | Full CV page |
| `styles.css` | Custom styling (colors, fonts) |

## How to publish on GitHub

### Step 1: Install Quarto
Download from https://quarto.org/docs/get-started/

### Step 2: Create your GitHub repo
- Go to github.com and create a new repo named: `yourusername.github.io`
- Or fork your friend's repo: github.com/mohdasti/quarto-website

### Step 3: Add your files
Copy all these files into the repo folder.

### Step 4: Add a profile photo
- Name it `profile.jpg` and put it in the same folder
- This will show on the About page

### Step 5: Render locally (optional preview)
```bash
quarto preview
```

### Step 6: Publish to GitHub Pages
```bash
quarto publish gh-pages
```
This builds the site and pushes it to GitHub Pages automatically.

Your site will be live at: `https://yourusername.github.io`

## Customization tips
- Update your Google Scholar link in `_quarto.yml` and `index.qmd`
- Add your GitHub profile link in `index.qmd`
- Replace `profile.jpg` with your actual photo
- To change colors, edit `styles.css` (look for `#1a3a5c`)
