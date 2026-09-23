# SPEC.md

## 1. TECHNOLOGY STACK

- Python 3.x
- Flask (minimal web framework)

## 2. DATA CONTRACTS

**Request**: No standalone model. Identification number passed as integer path parameter.

**Response (200 - exists)**:
```json
{
  "id": 12345,
  "nombre": "string",
  "existe": true
}
```

**Response (404 - not found)**:
```json
{
  "id": 12345,
  "existe": false
}
```

## 3. API ENDPOINTS

- `GET /identificacion/<int:id>`

## 4. FILE STRUCTURE

```
app.py
requirements.txt
```

**app.py**: Flask application with single endpoint. Greenfield implementation with in-memory mock data for basic identification records.

**requirements.txt**: Contains only `flask`.

## 5. ENVIRONMENT VARIABLES

None

## 6. IMPORT CONTRACTS

- Flask: `Flask`, `jsonify`, `abort`
- Route symbol: `app`

## 10. FUNCTIONAL REQUIREMENTS COVERAGE

| Literal Requirement | Implementation |
|---------------------|----------------|
| "Crear un endpoint que reciba un número de identificación" | `GET /identificacion/<int:id>` in `app.py` |
| "consulte si existe" | Logic checks in-memory dictionary for presence of id |
| "devolviendo sus datos básicos" | Returns JSON with `id`, `nombre`, `existe` fields |
| "numeor enteros" | Path parameter typed as `<int:id>` |
| "local" | Single `app.py` file, no deployment configuration |
| "todo es greenfield" | Minimal Flask app, no external dependencies beyond framework |