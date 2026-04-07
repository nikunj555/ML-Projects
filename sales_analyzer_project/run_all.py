import subprocess
import sys
import os

print("="*60)
print("🚀 SALES INTELLIGENCE PLATFORM")
print("="*60)

# Step 1: Generate data
print("\n📊 STEP 1: Generating data...")
subprocess.run([sys.executable, "fetch_superstore.py"])

# Step 2: Train model
print("\n🧠 STEP 2: Training model...")
subprocess.run([sys.executable, "train_model.py"])

print("\n" + "="*60)
print("✅ SETUP COMPLETE!")
print("="*60)
print("\n📌 NEXT STEPS:")
print("1. Start backend:  cd backend && uvicorn api:app --reload --port 8000")
print("2. Start frontend: streamlit run app.py")
print("\n📊 Dashboard: http://localhost:8501")
print("🔌 API Docs: http://localhost:8000/docs")