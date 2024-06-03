import hashlib

def hash(key) -> str:
  hasher = hashlib.sha256()
  to_bytes = key.encode("UTF-8")
  hasher.update(to_bytes)
  hashed_string = hasher.hexdigest()
  return hashed_string