#!/usr/bin/env python3
"""Fetch live token prices from Jupiter API."""

import requests
import sys

def get_price(token: str) -> float:
    """Get USD price for a token symbol."""
    url = f"https://price.jup.ag/v6/price?ids={token}"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    return float(data["data"][token]["price"])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: fetch_price.py <TOKEN>", file=sys.stderr)
        sys.exit(1)
    
    token = sys.argv[1].upper()
    try:
        price = get_price(token)
        print(f"{token}: ${price:.4f}")
    except Exception as e:
        print(f"Error fetching {token}: {e}", file=sys.stderr)
        sys.exit(1)