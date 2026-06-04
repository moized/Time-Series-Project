import os
import shutil
from pathlib import Path

def setup_elite_workspace():
    # 1. Proje kök dizinini otomatik tespit et
    root = Path.cwd()
    print(f"🚀 Refactoring started at: {root}\n")

    # 2. Hedef elit klasör şemasını tanımla
    dirs_to_create = [
        root / "data" / "raw",
        root / "notebooks",
        root / "reports" / "html",
        root / "reports" / "figures",
        root / "presentation",
        root / "archive" / "legacy_reports",
        root / "archive" / "temporary_scripts"
    ]

    for folder in dirs_to_create:
        folder.mkdir(parents=True, exist_ok=True)

    # 3. Ana veri setini taşı (Eğer kök dizindeyse)
    raw_csv = root / "teias_uretim_tuketim.csv"
    if raw_csv.exists():
        shutil.move(str(raw_csv), str(root / "data" / "raw" / "teias_uretim_tuketim.csv"))
        print("📁 Moved master dataset to data/raw/")

    # 4. Ana analiz notebook'unu taşı (Eğer kök dizindeyse)
    master_nb = root / "teias_report.ipynb"
    if master_nb.exists():
        shutil.move(str(master_nb), str(root / "notebooks" / "teias_report.ipynb"))
        print("📓 Moved master notebook to notebooks/")

    # 5. Eski/Mükerrer rapor klasörlerini güvenle arşive kaldır
    legacy_folders = ["report1", "report2"]
    for folder_name in legacy_folders:
        legacy_path = root / folder_name
        if legacy_path.exists() and legacy_path.is_dir():
            # Eğer hedefte zaten varsa silip taşımak için güvenlik kontrolü
            target_path = root / "archive" / "legacy_reports" / folder_name
            if target_path.exists():
                shutil.rmtree(target_path)
            shutil.move(str(legacy_path), str(target_path))
            print(f"📦 Archived duplicate folder: {folder_name}/")

    # 6. Presentation altındaki kalabalığı temizle
    pres_dir = root / "presentation"
    if pres_dir.exists() and pres_dir.is_dir():
        for item in pres_dir.iterdir():
            # Sadece ana sunumu koru, geri kalan her şeyi arşive taşı
            if item.is_file() and item.name != "TEIAS_Final_Sunum.pptx":
                target_script = root / "archive" / "temporary_scripts" / item.name
                if target_script.exists():
                    item.unlink() # Mükerrer ise yerel dosyayı temizle
                else:
                    shutil.move(str(item), str(target_script))
        print("✨ Sanitized presentation/ folder. Kept ONLY TEIAS_Final_Sunum.pptx")

    # 7. Otomatik master .gitignore dosyasını yaz
    gitignore_content = """# ==========================================
# 1. Core Environment & Jupyter Checkpoints
# ==========================================
__pycache__/
.ipynb_checkpoints/
*/.ipynb_checkpoints/*
.venv/
bdv_env/
.pytest_cache/
*.exe

# ==========================================
# 2. Local Untracked Archive Layer
# ==========================================
/archive/

# ==========================================
# 3. Data File Protection (Keep Sheets Local)
# ==========================================
*.csv
*.xlsx
/data/
"""
    with open(root / ".gitignore", "w", encoding="utf-8") as f:
        f.write(gitignore_content)
    print("📝 Generated production-grade .gitignore")

    print("\n🟢 Refactoring completed successfully! Your workspace is now clean.")

if __name__ == "__main__":
    setup_elite_workspace()