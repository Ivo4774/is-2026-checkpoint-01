#La imagen que nos piden
FROM python:3.12-slim

# 2. Establecer una carpeta de trabajo dentro del contenedor
WORKDIR /app

# 3. Capas cacheadas: Copiar SOLO requirements primero y descargar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el resto del código (app.py)
COPY app.py .

# 5. Usuario no-root por seguridad
RUN useradd -m appuser
RUN chown -R appuser:appuser /app
USER appuser

# 6. Defino el puerto que va a usar
EXPOSE 5000

# 7. HEALTHCHECK apuntando a /api/health
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/api/health')" || exit 1

# 8. Comando para encender el servidor con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]