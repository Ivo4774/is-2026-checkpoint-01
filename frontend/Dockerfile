#Imagen base slim y directorio de trabajo
FROM python:3.12-slim
WORKDIR /app

COPY html/ ./html/
EXPOSE 8080

#Servidor HTTP
CMD ["python3", "-m", "http.server", "8080", "--directory", "html"]