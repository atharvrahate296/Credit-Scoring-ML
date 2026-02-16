import kagglehub

# Download latest version
path = kagglehub.dataset_download("lihxlhx/give-me-some-credit")
print("Path to dataset files:", path)

path = kagglehub.dataset_download("prena0808/statlog-german-credit-data")
print("Path to dataset files:", path)

path = kagglehub.dataset_download("megancrenshaw/home-credit-default-risk")
print("Path to dataset files:", path)

path = kagglehub.dataset_download("adarshsng/lending-club-loan-data-csv")
print("Path to dataset files:", path)