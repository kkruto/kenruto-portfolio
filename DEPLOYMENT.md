# Deployment Guide

This guide covers how to deploy your Django portfolio website to various hosting platforms.

## ⚠️ Important: GitHub Pages Won't Work

**GitHub Pages only supports static websites (HTML, CSS, JavaScript).** This is a Django (Python) application that requires a server to run. You need a hosting platform that supports Python backends.

---

## 🚀 Quick Start - Run Locally

### Prerequisites
- Python 3.11+
- Node.js and npm
- Git

### Setup Steps

1. **Clone and navigate to repository:**
   ```bash
   cd kenruto-portfolio
   ```

2. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   # OR
   venv\Scripts\activate  # Windows
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Node dependencies:**
   ```bash
   npm install
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Populate dummy data (optional):**
   ```bash
   python manage.py populate_dummy_data
   ```

7. **Create admin user:**
   ```bash
   python manage.py createsuperuser
   ```

8. **Start development servers (2 terminals needed):**

   **Terminal 1 - Tailwind CSS:**
   ```bash
   npm run dev
   ```

   **Terminal 2 - Django:**
   ```bash
   python manage.py runserver
   ```

9. **View site:**
   - Frontend: http://localhost:8000
   - Admin: http://localhost:8000/admin

---

## 🌐 Production Deployment Options

### Option 1: Railway (Recommended - Free Tier)

**Best for:** Quick deployment, automatic GitHub sync, built-in PostgreSQL

#### Setup Steps:

1. **Sign up at [railway.app](https://railway.app)** using your GitHub account

2. **Create new project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `kenruto-portfolio`

3. **Add PostgreSQL database:**
   - In your project, click "New" → "Database" → "Add PostgreSQL"
   - Railway automatically provides `DATABASE_URL`

4. **Configure environment variables:**

   Go to project settings → Variables, add:
   ```
   SECRET_KEY=django-insecure-GENERATE-NEW-KEY-HERE
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.railway.app
   ```

5. **Generate SECRET_KEY:**
   ```python
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

6. **Configure build settings:**
   - Build command: `python manage.py migrate && npm install && npm run build && python manage.py collectstatic --noinput`
   - Start command: `gunicorn portfolio.wsgi`

7. **Deploy:**
   - Railway auto-deploys on every push to your GitHub repo
   - Get your URL from Railway dashboard

#### Pros:
- ✅ Free tier with 500 hours/month
- ✅ Automatic deployments from GitHub
- ✅ Built-in PostgreSQL
- ✅ Easy environment variable management
- ✅ Custom domain support

#### Cons:
- ⚠️ Free tier has usage limits

---

### Option 2: Render (Free Tier)

**Best for:** Simple setup, generous free tier

#### Setup Steps:

1. **Sign up at [render.com](https://render.com)** with GitHub

2. **Create PostgreSQL database:**
   - Click "New +" → "PostgreSQL"
   - Name it (e.g., `kenruto-portfolio-db`)
   - Copy the "Internal Database URL"

3. **Create web service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name:** kenruto-portfolio
     - **Environment:** Python 3
     - **Build Command:**
       ```bash
       pip install -r requirements.txt && npm install && npm run build && python manage.py migrate && python manage.py collectstatic --noinput
       ```
     - **Start Command:**
       ```bash
       gunicorn portfolio.wsgi:application
       ```

4. **Add environment variables:**
   ```
   PYTHON_VERSION=3.11.0
   SECRET_KEY=your-generated-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-app-name.onrender.com
   DATABASE_URL=<paste-internal-database-url>
   ```

5. **Deploy:**
   - Click "Create Web Service"
   - Render will build and deploy automatically

#### Pros:
- ✅ Generous free tier
- ✅ Auto-deploy from GitHub
- ✅ Good documentation
- ✅ Custom domain support

#### Cons:
- ⚠️ Free tier services spin down after inactivity (slower first load)

---

### Option 3: Heroku (Paid)

**Best for:** Established platform, lots of add-ons

**Note:** Heroku no longer has a free tier ($5-7/month minimum)

#### Setup Steps:

1. **Install Heroku CLI:**
   ```bash
   # Mac
   brew tap heroku/brew && brew install heroku

   # Windows
   # Download from https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Login to Heroku:**
   ```bash
   heroku login
   ```

3. **Create Heroku app:**
   ```bash
   heroku create kenruto-portfolio
   ```

4. **Add PostgreSQL:**
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```

5. **Set environment variables:**
   ```bash
   heroku config:set SECRET_KEY="your-generated-secret-key"
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=kenruto-portfolio.herokuapp.com
   ```

6. **Deploy:**
   ```bash
   git push heroku main
   ```

7. **Run migrations:**
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

#### Pros:
- ✅ Mature platform
- ✅ Many add-ons available
- ✅ Excellent documentation

#### Cons:
- ⚠️ No free tier
- ⚠️ More expensive than alternatives

---

### Option 4: DigitalOcean App Platform

**Best for:** Scalability, more control

#### Setup Steps:

1. **Sign up at [digitalocean.com](https://www.digitalocean.com/)**

2. **Create new app:**
   - Click "Create" → "Apps"
   - Connect your GitHub repository

3. **Configure app:**
   - **Build Command:**
     ```bash
     pip install -r requirements.txt && npm install && npm run build && python manage.py collectstatic --noinset
     ```
   - **Run Command:**
     ```bash
     gunicorn portfolio.wsgi
     ```

4. **Add managed database:**
   - In app settings, add PostgreSQL database
   - Copy `DATABASE_URL`

5. **Set environment variables:**
   ```
   SECRET_KEY=your-secret-key
   DEBUG=False
   ALLOWED_HOSTS=your-app.ondigitalocean.app
   DATABASE_URL=<provided-by-digitalocean>
   ```

#### Pricing:
- Starting at $5/month for basic tier

---

## 📋 Pre-Deployment Checklist

Before deploying to production:

### 1. Security Settings

- [ ] Generate new `SECRET_KEY` (never use development key in production)
- [ ] Set `DEBUG=False` in production environment
- [ ] Configure `ALLOWED_HOSTS` with your domain
- [ ] Enable HTTPS redirect in `settings.py`:
  ```python
  SECURE_SSL_REDIRECT = True
  SESSION_COOKIE_SECURE = True
  CSRF_COOKIE_SECURE = True
  ```

### 2. Database Migration

- [ ] Set up PostgreSQL database (don't use SQLite in production)
- [ ] Configure `DATABASE_URL` environment variable
- [ ] Run migrations: `python manage.py migrate`

### 3. Static Files

- [ ] Build Tailwind CSS: `npm run build`
- [ ] Collect static files: `python manage.py collectstatic`
- [ ] Verify WhiteNoise is configured in `settings.py`

### 4. Media Files

**Current setup:** Media files stored locally (not suitable for production)

**Recommended:** Use cloud storage (S3, Cloudinary, etc.)

**To set up AWS S3:**

1. Install in `requirements.txt` (already included):
   ```
   django-storages
   boto3
   ```

2. Create S3 bucket on AWS

3. Add to `settings.py`:
   ```python
   if not DEBUG:
       AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
       AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
       AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
       AWS_S3_REGION_NAME = config('AWS_S3_REGION_NAME', default='us-east-1')
       AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

       DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
       MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
   ```

4. Set environment variables:
   ```
   AWS_ACCESS_KEY_ID=your-key
   AWS_SECRET_ACCESS_KEY=your-secret
   AWS_STORAGE_BUCKET_NAME=your-bucket-name
   AWS_S3_REGION_NAME=us-east-1
   ```

### 5. Email Configuration

**Current setup:** Console backend (prints to console, development only)

**For production**, choose an email service:

#### Option A: Gmail SMTP
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')  # Use App Password
```

#### Option B: SendGrid
```bash
pip install sendgrid
```
```python
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = config('SENDGRID_API_KEY')
```

### 6. Environment Variables

Copy `.env.example` to `.env` and fill in:

```bash
cp .env.example .env
```

**Required variables:**
- `SECRET_KEY` - Generate new one for production
- `DEBUG` - Set to `False`
- `ALLOWED_HOSTS` - Your domain(s)
- `DATABASE_URL` - PostgreSQL connection string

**Optional but recommended:**
- `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` - For email
- `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` - For S3 media storage

### 7. Custom Domain Setup

After deploying:

1. **Purchase domain** (Namecheap, Google Domains, etc.)

2. **Add DNS records:**
   - Type: CNAME
   - Name: @ (or www)
   - Value: your-app.railway.app (or whatever your host provides)

3. **Update `ALLOWED_HOSTS` in environment variables:**
   ```
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   ```

4. **Set up SSL certificate** (most platforms do this automatically)

---

## 🔧 Common Deployment Issues

### Issue: Static files not loading

**Solution:**
```bash
python manage.py collectstatic --noinput
```

Verify in `settings.py`:
```python
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Issue: Database connection error

**Solution:**
- Verify `DATABASE_URL` is set correctly
- Check PostgreSQL is running
- Run migrations: `python manage.py migrate`

### Issue: 500 Internal Server Error

**Solution:**
- Check platform logs (Railway/Render dashboard)
- Verify all environment variables are set
- Ensure `DEBUG=False` (but check logs for specific error)

### Issue: CSS not compiling

**Solution:**
```bash
npm install
npm run build
python manage.py collectstatic --noinput
```

---

## 📊 Recommended Setup for Your Portfolio

**For simplicity and cost:**

1. **Hosting:** Railway or Render (free tier)
2. **Database:** Platform-provided PostgreSQL
3. **Media Storage:** Start with local, migrate to S3 when needed
4. **Email:** Gmail SMTP or SendGrid
5. **Domain:** Purchase custom domain ($10-15/year)

**Estimated monthly cost:** $0 (free tier) to $5 (if you upgrade)

---

## 📚 Additional Resources

- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)
- [Railway Documentation](https://docs.railway.app/)
- [Render Django Guide](https://render.com/docs/deploy-django)
- [Heroku Django Guide](https://devcenter.heroku.com/articles/django-app-configuration)

---

## 🎯 Quick Deployment Summary

**Fastest path to live site:**

1. Sign up for Railway (free)
2. Connect GitHub repo
3. Add PostgreSQL database
4. Set environment variables (SECRET_KEY, DEBUG, ALLOWED_HOSTS)
5. Deploy (automatic)
6. Run migrations via Railway terminal
7. Get your live URL

**Total time:** ~15 minutes

---

**Need help?** Check the platform-specific documentation or open an issue in the repository.
