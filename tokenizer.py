# Imports
import re

# Define Tokens
TOKEN_TYPES = [
  ('NUMBER', r'\d+'),                                          # 정수
  ('IDENTIFIER', r'[가-힣\w]+'),                        	     # 식별자 (한글 및 영문자)
  ('KEYWORD', r'\b(키워드)\b'),  															 # 한국어 키워드
  ('OPERATOR', r'[=+\-*/<>!]+'),                               # 연산자
  ('PARENTHESIS', r'[(){}[\]]'),                               # 괄호
  ('COMMA', r','),                                          	 # 쉼표
  ('SEMICOLON', r';'),                                     	 	 # 세미콜론
  ('STRING', r'"(.*?)"'),                                  		 # 문자열 리터럴
  ('COMMENT', r'#.*'),                                      	 # 주석
  ('WHITESPACE', r'\s+'),                                   	 # 공백
]


def tokenize(code):
  tokens = []
  while code:
    match = None
    for token_type, pattern in TOKEN_TYPES:
      regex = re.compile(pattern)
      match = regex.match(code)
      if match:
        tokens.append((token_type, match.group(0)))
        code = code[match.end():]
        break
    if not match:
      raise SyntaxError(f"Unexpected token: {code[0]}")
  return tokens