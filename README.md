# HTB Readme Stats

Static Hack The Box stats cards for GitHub README files.

This project generates an SVG card with GitHub Actions and publishes it through GitHub Pages. No Vercel, Render, serverless API, or backend hosting required.

## Setup

1. Create a new public repo, for example `htb-readme-stats`.
2. Upload this project.
3. Go to `Settings → Pages`.
4. Select `Deploy from a branch`.
5. Use `main` and `/ (root)`.
6. Go to `Settings → Secrets and variables → Actions`.
7. Add repository variable `HTB_USER=1132645`.
8. Optional: add repository variable `HTB_THEME=purple`.
9. Optional: add repository secret `HTB_TOKEN=<your HTB app token>`.
10. Run `Actions → Update HTB README Stats → Run workflow`.

## README snippet

```html
<p align="center">
  <a href="https://app.hackthebox.com/public/users/1132645">
    <img width="70%" src="https://ZLCube.github.io/htb-readme-stats/public/htb/card.svg" alt="Hack The Box stats" />
  </a>
</p>
```

Available themes: `purple`, `htb`, `dark`.

## Local usage

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
htb-readme-stats --user 1132645 --theme purple
```

Generated files:

```txt
public/htb/1132645.svg
public/htb/1132645.json
public/htb/card.svg
public/htb/profile.json
```
