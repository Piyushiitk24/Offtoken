# 🚀 Deployment Guide for TokenForge

This guide covers multiple deployment options for TokenForge, from local development to production cloud deployment.

## 🏠 Local Development

### Quick Start (Recommended)
```bash
# Clone the repository
git clone https://github.com/Piyushiitk24/Offtoken.git
cd Offtoken

# One-command setup and launch
python3 setup.py
```

### Manual Setup
```bash
# Install system dependencies (macOS)
brew install tesseract poppler

# Setup Python environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Launch application
streamlit run app.py
```

## 🌐 GitHub Pages (Static Landing)

The repository includes a beautiful landing page that automatically deploys to GitHub Pages.

### Setup
1. Go to your GitHub repository settings
2. Navigate to "Pages" in the sidebar
3. Set source to "GitHub Actions"
4. The landing page will be available at: `https://yourusername.github.io/Offtoken`

### Features
- ✨ Beautiful PRIDE-themed design
- 📱 Fully responsive
- 🚀 Fast loading
- 🔗 Links to local deployment instructions

## ☁️ Streamlit Cloud Deployment

Deploy your Streamlit app to Streamlit Cloud for easy sharing.

### Setup
1. Fork the repository on GitHub
2. Sign up for [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub account
4. Select your forked repository
5. Set main file path: `app.py`
6. Deploy!

### Configuration
- **Python version**: 3.11
- **Main file**: `app.py`
- **Requirements**: `requirements.txt`
- **Secrets**: Not required (app works without API keys)

## 🐳 Docker Deployment

### Build and Run Locally
```bash
# Build the Docker image
docker build -t tokenforge .

# Run the container
docker run -p 8501:8501 tokenforge
```

### Using Docker Compose
```bash
# Start the application
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the application
docker-compose down
```

### Production Docker Deployment
```bash
# For production with specific tag
docker build -t tokenforge:v1.0.0 .
docker run -d \
  --name tokenforge-prod \
  --restart unless-stopped \
  -p 8501:8501 \
  tokenforge:v1.0.0
```

## ☁️ Cloud Platform Deployment

### Heroku
1. Install Heroku CLI
2. Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```
3. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

### Google Cloud Run
```bash
# Build and deploy
gcloud run deploy tokenforge \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### AWS ECS/Fargate
1. Push image to ECR
2. Create ECS task definition
3. Deploy to Fargate cluster

### Azure Container Instances
```bash
az container create \
  --resource-group myResourceGroup \
  --name tokenforge \
  --image your-registry/tokenforge:latest \
  --ports 8501 \
  --dns-name-label tokenforge-unique
```

## 🔧 Environment Configuration

### Production Environment Variables
```bash
# Streamlit configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Optional: Performance tuning
STREAMLIT_SERVER_MAX_UPLOAD_SIZE=200
STREAMLIT_SERVER_ENABLE_CORS=false
```

### Security Configuration
- ✅ No API keys required
- ✅ All processing is local
- ✅ No external data transmission
- ✅ CORS disabled for security
- ✅ XSRF protection enabled

## 📊 Monitoring and Health Checks

### Health Check Endpoint
```bash
curl http://localhost:8501/_stcore/health
```

### Docker Health Check
The Docker image includes built-in health checks:
```dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1
```

### Monitoring
- **Logs**: Check Docker/Streamlit logs for errors
- **Metrics**: Monitor memory usage and response times
- **Uptime**: Use external monitoring services

## 🚀 Performance Optimization

### Resource Requirements
- **Minimum**: 512MB RAM, 1 CPU core
- **Recommended**: 1GB RAM, 2 CPU cores
- **Storage**: 2GB for dependencies

### Optimization Tips
1. **Memory**: Use Docker multi-stage builds
2. **Speed**: Enable caching in Streamlit
3. **Size**: Minimize image layers
4. **Security**: Run as non-root user

## 🔍 Troubleshooting

### Common Issues

**Port already in use:**
```bash
# Kill process on port 8501
lsof -ti:8501 | xargs kill -9
```

**Docker build fails:**
```bash
# Clean build with no cache
docker build --no-cache -t tokenforge .
```

**Streamlit crashes:**
```bash
# Check logs
docker logs tokenforge-container-name
```

**Missing dependencies:**
```bash
# Rebuild with fresh requirements
pip install --upgrade -r requirements.txt
```

## 📈 Scaling for Production

### Load Balancing
```yaml
# nginx.conf example
upstream tokenforge {
    server tokenforge1:8501;
    server tokenforge2:8501;
    server tokenforge3:8501;
}

server {
    listen 80;
    location / {
        proxy_pass http://tokenforge;
    }
}
```

### Kubernetes Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tokenforge
spec:
  replicas: 3
  selector:
    matchLabels:
      app: tokenforge
  template:
    metadata:
      labels:
        app: tokenforge
    spec:
      containers:
      - name: tokenforge
        image: tokenforge:latest
        ports:
        - containerPort: 8501
        resources:
          limits:
            memory: "1Gi"
            cpu: "500m"
          requests:
            memory: "512Mi"
            cpu: "250m"
```

## 🔒 Security Best Practices

1. **Container Security**:
   - Run as non-root user
   - Use minimal base images
   - Regular security updates

2. **Network Security**:
   - Use HTTPS in production
   - Implement rate limiting
   - Enable XSRF protection

3. **Data Security**:
   - All processing is local
   - No data persistence by default
   - Automatic cleanup of temporary files

## 📞 Support

If you encounter issues during deployment:

1. **Check logs** first
2. **Review configuration** files
3. **Test locally** before deploying
4. **Create an issue** on GitHub with:
   - Deployment method used
   - Error messages
   - System specifications
   - Steps to reproduce

---

**Happy Deploying! 🚀**

Choose the deployment method that best fits your needs. All options provide the same great TokenForge experience with beautiful PRIDE-themed UI.
