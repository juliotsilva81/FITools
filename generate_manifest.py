import os
import json
import hashlib
from datetime import datetime, timezone

def generate_file_hash(filepath):
    """Gera um hash SHA-256 para garantir a integridade do arquivo."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def build_manifest(base_dir):
    manifest = {
        "version": "1.0.1", # Atualize a versão aqui quando fizer grandes lançamentos
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "files": []
    }
    
    for root, _, files in os.walk(base_dir):
        for file in files:
            # Ignorar a pasta do git, caches, arquivos ocultos e o próprio manifesto para evitar loops
            if ".git" in root or "__pycache__" in root or file in ["manifest.json", "generate_manifest.py", "desktop.ini"]:
                continue
                
            filepath = os.path.join(root, file)
            # Salva o caminho relativo com barras normais (padrão web)
            rel_path = os.path.relpath(filepath, base_dir).replace("\\", "/")
            
            manifest["files"].append({
                "path": rel_path,
                "hash": generate_file_hash(filepath),
                "size": os.path.getsize(filepath)
            })
            
    return manifest

if __name__ == "__main__":
    # Define o diretório base como sendo a raiz onde o script está
    base_directory = os.path.dirname(os.path.abspath(__file__))
    manifest_data = build_manifest(base_directory)
    
    manifest_path = os.path.join(base_directory, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=4)
        
    print(f"Manifesto gerado com sucesso com {len(manifest_data['files'])} arquivos em:\n{manifest_path}")