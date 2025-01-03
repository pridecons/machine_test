import os
from kiteconnect import KiteConnect
from flask import Flask, jsonify
from config import API_KEY, API_SECRET

ACCESS_TOKEN_FILE = "access_token.txt"


