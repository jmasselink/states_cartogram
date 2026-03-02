# Recreate the venv for ARM64
uv venv ~/Documents/code/python/venv/cartogram --python python3.13

# Activate it
source ~/Documents/code/python/venv/cartogram/bin/activate

# Install all packages
uv pip install -r ~/Documents/code/python/states_cartogram/requirements.txt