# Docker Management Script for Saad Siddique Portfolio Website
# Run this script to manage your Docker container

Write-Host "=== Saad Siddique Portfolio Website - Docker Management ===" -ForegroundColor Green
Write-Host ""

# Check if container is running
$containerStatus = docker ps --filter "name=saad-portfolio-website" --format "table {{.Names}}\t{{.Status}}"
if ($containerStatus -match "saad-portfolio-website") {
    Write-Host "✅ Container Status: RUNNING" -ForegroundColor Green
    Write-Host $containerStatus
} else {
    Write-Host "❌ Container Status: NOT RUNNING" -ForegroundColor Red
}

Write-Host ""
Write-Host "Available Images:" -ForegroundColor Yellow
docker images --filter "reference=*portfolio*" --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}\t{{.CreatedAt}}"

Write-Host ""
Write-Host "Commands:" -ForegroundColor Yellow
Write-Host "  Start:   docker start saad-portfolio-website"
Write-Host "  Stop:    docker stop saad-portfolio-website"
Write-Host "  Restart: docker restart saad-portfolio-website"
Write-Host "  Logs:    docker logs saad-portfolio-website"
Write-Host "  Remove:  docker rm -f saad-portfolio-website"
Write-Host ""
Write-Host "Website URL: http://localhost:5000" -ForegroundColor Cyan
