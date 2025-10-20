# JSON Syntax Compliance Guide

## Table of Contents
1. [Basic JSON Structure Requirements](#basic-json-structure-requirements)
2. [Proper Use of Quotes](#proper-use-of-quotes)
3. [Data Types and Formatting](#data-types-and-formatting)
4. [Array Syntax Rules](#array-syntax-rules)
5. [Object Syntax Rules](#object-syntax-rules)
6. [Comma Placement and Usage](#comma-placement-and-usage)
7. [Nesting Guidelines](#nesting-guidelines)
8. [Common Pitfalls to Avoid](#common-pitfalls-to-avoid)
9. [Best Practices for Readability](#best-practices-for-readability)
10. [Validation and Testing](#validation-and-testing)

---

## Basic JSON Structure Requirements

### Fundamental Rules
JSON (JavaScript Object Notation) is a lightweight data interchange format that follows strict syntax rules:

1. **Root Element**: JSON must have exactly one root element (object or array)
2. **Case Sensitivity**: JSON is case-sensitive for all keys and values
3. **Character Encoding**: JSON text must be encoded in UTF-8, UTF-16, or UTF-32
4. **Whitespace**: Spaces, tabs, line feeds, and carriage returns are allowed between tokens

### Valid Root Structures
```json
// Valid: Object as root
{
  "name": "example",
  "value": 42
}

// Valid: Array as root
[
  {"id": 1, "name": "first"},
  {"id": 2, "name": "second"}
]

// Invalid: Multiple root elements
{
  "first": "object"
}
{
  "second": "object"
}

// Invalid: Primitive as root (in strict JSON)
"just a string"
42
true
```

---

## Proper Use of Quotes

### Key Quoting Rules
1. **Object Keys**: MUST always be enclosed in double quotes
2. **String Values**: MUST always be enclosed in double quotes
3. **Quote Type**: ONLY double quotes (`"`) are allowed, never single quotes (`'`)

### Correct Quote Usage
```json
{
  "name": "John Doe",           // ✓ Correct: double quotes for key and string value
  "age": 30,                    // ✓ Correct: no quotes for number
  "isActive": true,             // ✓ Correct: no quotes for boolean
  "address": null               // ✓ Correct: no quotes for null
}
```

### Incorrect Quote Usage
```json
{
  name: "John Doe",             // ✗ Wrong: key without quotes
  'name': "John Doe",           // ✗ Wrong: single quotes for key
  "name": 'John Doe',           // ✗ Wrong: single quotes for string value
  "name": "John Doe",           // ✗ Wrong: smart quotes
  "age": "30"                   // ✗ Wrong: number as string (unless intended)
}
```

### Escaping Special Characters
```json
{
  "message": "He said, \"Hello, World!\"",     // Escape double quotes
  "path": "C:\\Users\\Documents\\file.txt",    // Escape backslashes
  "newline": "Line 1\nLine 2",                 // Newline character
  "tab": "Column1\tColumn2",                   // Tab character
  "unicode": "Caf\u00e9"                       // Unicode escape
}
```

---

## Data Types and Formatting

### String Values
```json
{
  "emptyString": "",
  "normalString": "Hello, World!",
  "stringWithEscapes": "Line 1\nLine 2\tTabbed",
  "unicodeString": "Caf\u00e9 \u2603",
  "quotedString": "She said \"Hello\""
}
```

### Number Values
```json
{
  "integer": 42,
  "negativeInteger": -17,
  "float": 3.14159,
  "negativeFloat": -2.5,
  "exponential": 1.23e10,
  "negativeExponential": -1.23e-4,
  "zero": 0,
  "negativeZero": -0
}
```

### Invalid Number Formats
```json
{
  "leadingZero": 042,           // ✗ Wrong: leading zeros not allowed
  "hexadecimal": 0xFF,          // ✗ Wrong: hex not supported
  "infinity": Infinity,         // ✗ Wrong: Infinity not supported
  "notANumber": NaN,            // ✗ Wrong: NaN not supported
  "trailingComma": 42.,         // ✗ Wrong: trailing decimal point
  "leadingDecimal": .42         // ✗ Wrong: leading decimal point
}
```

### Boolean Values
```json
{
  "isTrue": true,               // ✓ Correct: lowercase true
  "isFalse": false,             // ✓ Correct: lowercase false
  "notTrue": True,              // ✗ Wrong: capitalized
  "notFalse": FALSE             // ✗ Wrong: all caps
}
```

### Null Values
```json
{
  "nullValue": null,            // ✓ Correct: lowercase null
  "notNull": NULL,              // ✗ Wrong: uppercase
  "notUndefined": undefined     // ✗ Wrong: undefined not supported
}
```

---

## Array Syntax Rules

### Basic Array Structure
```json
{
  "emptyArray": [],
  "numberArray": [1, 2, 3, 4, 5],
  "stringArray": ["apple", "banana", "cherry"],
  "mixedArray": [1, "two", true, null],
  "nestedArrays": [[1, 2], [3, 4], [5, 6]]
}
```

### Array Formatting Rules
1. **Square Brackets**: Arrays must be enclosed in `[` and `]`
2. **Element Separation**: Elements separated by commas
3. **No Trailing Comma**: Last element must NOT have a trailing comma
4. **Mixed Types**: Arrays can contain different data types

### Correct Array Examples
```json
{
  "singleElement": [42],
  "multipleElements": [1, 2, 3],
  "objectsInArray": [
    {"id": 1, "name": "first"},
    {"id": 2, "name": "second"}
  ],
  "nestedStructure": [
    {
      "category": "fruits",
      "items": ["apple", "banana"]
    },
    {
      "category": "vegetables",
      "items": ["carrot", "broccoli"]
    }
  ]
}
```

### Incorrect Array Examples
```json
{
  "trailingComma": [1, 2, 3,],          // ✗ Wrong: trailing comma
  "missingComma": [1 2 3],              // ✗ Wrong: missing commas
  "wrongBrackets": (1, 2, 3),           // ✗ Wrong: parentheses instead of brackets
  "extraComma": [1,, 3]                 // ✗ Wrong: double comma
}
```

---

## Object Syntax Rules

### Basic Object Structure
```json
{
  "emptyObject": {},
  "simpleObject": {
    "key1": "value1",
    "key2": "value2"
  },
  "nestedObject": {
    "level1": {
      "level2": {
        "level3": "deep value"
      }
    }
  }
}
```

### Object Formatting Rules
1. **Curly Braces**: Objects must be enclosed in `{` and `}`
2. **Key-Value Pairs**: Each pair consists of a key and value separated by `:`
3. **Pair Separation**: Key-value pairs separated by commas
4. **No Trailing Comma**: Last pair must NOT have a trailing comma
5. **Unique Keys**: Keys within an object must be unique

### Correct Object Examples
```json
{
  "user": {
    "id": 123,
    "profile": {
      "firstName": "John",
      "lastName": "Doe",
      "email": "john.doe@example.com",
      "preferences": {
        "theme": "dark",
        "notifications": true,
        "language": "en"
      }
    },
    "roles": ["user", "admin"],
    "lastLogin": "2023-12-01T10:30:00Z"
  }
}
```

### Incorrect Object Examples
```json
{
  "trailingComma": {
    "key1": "value1",
    "key2": "value2",              // ✗ Wrong: trailing comma
  },
  "missingColon": {
    "key1" "value1"                // ✗ Wrong: missing colon
  },
  "duplicateKeys": {
    "name": "first",
    "name": "second"               // ✗ Wrong: duplicate keys
  },
  "unquotedKey": {
    name: "value"                  // ✗ Wrong: unquoted key
  }
}
```

---

## Comma Placement and Usage

### Comma Rules
1. **Separator Only**: Commas separate elements, never terminate them
2. **No Leading Commas**: Never start with a comma
3. **No Trailing Commas**: Never end with a comma
4. **No Double Commas**: Never use consecutive commas

### Correct Comma Usage
```json
{
  "array": [1, 2, 3],
  "object": {
    "a": 1,
    "b": 2,
    "c": 3
  },
  "mixed": [
    {"id": 1, "name": "first"},
    {"id": 2, "name": "second"},
    {"id": 3, "name": "third"}
  ]
}
```

### Incorrect Comma Usage
```json
{
  "trailingInArray": [1, 2, 3,],        // ✗ Wrong: trailing comma
  "trailingInObject": {
    "a": 1,
    "b": 2,                             // ✗ Wrong: trailing comma
  },
  "leadingComma": [,1, 2, 3],           // ✗ Wrong: leading comma
  "doubleComma": [1,, 3],               // ✗ Wrong: double comma
  "missingComma": [1 2 3]               // ✗ Wrong: missing comma
}
```

---

## Nesting Guidelines

### Maximum Nesting Depth
- **Recommended**: Keep nesting under 5 levels deep
- **Maximum**: Most parsers support up to 20+ levels
- **Performance**: Deeper nesting impacts parsing performance

### Proper Nesting Structure
```json
{
  "level1": {
    "level2": {
      "level3": {
        "level4": {
          "level5": "This is getting deep"
        }
      }
    }
  },
  "betterStructure": {
    "users": [
      {
        "id": 1,
        "profile": {
          "name": "John",
          "settings": {
            "theme": "dark"
          }
        }
      }
    ]
  }
}
```

### Nesting Best Practices
```json
{
  "config": {
    "database": {
      "host": "localhost",
      "port": 5432,
      "credentials": {
        "username": "admin",
        "password": "secret"
      }
    },
    "api": {
      "version": "v1",
      "endpoints": {
        "users": "/api/v1/users",
        "posts": "/api/v1/posts"
      }
    }
  }
}
```

---

## Common Pitfalls to Avoid

### 1. Trailing Commas
```json
// ✗ Wrong
{
  "name": "John",
  "age": 30,
}

// ✓ Correct
{
  "name": "John",
  "age": 30
}
```

### 2. Single Quotes
```json
// ✗ Wrong
{
  'name': 'John',
  "age": 30
}

// ✓ Correct
{
  "name": "John",
  "age": 30
}
```

### 3. Unquoted Keys
```json
// ✗ Wrong
{
  name: "John",
  age: 30
}

// ✓ Correct
{
  "name": "John",
  "age": 30
}
```

### 4. Comments
```json
// ✗ Wrong - JSON doesn't support comments
{
  "name": "John", // This is a comment
  /* Multi-line comment */
  "age": 30
}

// ✓ Correct - No comments
{
  "name": "John",
  "age": 30
}
```

### 5. Functions and Undefined
```json
// ✗ Wrong
{
  "callback": function() { return true; },
  "value": undefined
}

// ✓ Correct
{
  "callback": "function_name",
  "value": null
}
```

### 6. Date Objects
```json
// ✗ Wrong
{
  "created": new Date()
}

// ✓ Correct
{
  "created": "2023-12-01T10:30:00Z"
}
```

### 7. Circular References
```json
// ✗ Wrong - Cannot represent circular references
{
  "parent": {
    "child": {
      "parent": /* reference to parent object */
    }
  }
}

// ✓ Correct - Use IDs for references
{
  "parent": {
    "id": "parent-1",
    "child": {
      "id": "child-1",
      "parentId": "parent-1"
    }
  }
}
```

---

## Best Practices for Readability

### 1. Consistent Indentation
```json
{
  "user": {
    "id": 123,
    "profile": {
      "name": "John Doe",
      "email": "john@example.com"
    },
    "preferences": {
      "theme": "dark",
      "language": "en"
    }
  }
}
```

### 2. Logical Key Ordering
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "created": "2023-01-01T00:00:00Z",
  "updated": "2023-12-01T10:30:00Z",
  "isActive": true,
  "roles": ["user", "admin"],
  "profile": {
    "firstName": "John",
    "lastName": "Doe",
    "avatar": "https://example.com/avatar.jpg"
  }
}
```

### 3. Meaningful Key Names
```json
{
  "userId": 123,                    // ✓ Clear and specific
  "userFirstName": "John",          // ✓ Descriptive
  "userLastLoginTimestamp": "2023-12-01T10:30:00Z",  // ✓ Explicit
  "isUserAccountActive": true       // ✓ Boolean prefix
}
```

### 4. Consistent Naming Conventions
```json
{
  "camelCase": {
    "firstName": "John",
    "lastName": "Doe",
    "emailAddress": "john@example.com"
  },
  "snake_case": {
    "first_name": "John",
    "last_name": "Doe",
    "email_address": "john@example.com"
  },
  "kebab-case": {
    "first-name": "John",
    "last-name": "Doe",
    "email-address": "john@example.com"
  }
}
```

### 5. Array vs Object Usage
```json
{
  "orderedList": [                  // ✓ Use array for ordered data
    "first",
    "second",
    "third"
  ],
  "keyValuePairs": {                // ✓ Use object for key-value relationships
    "primary": "#007bff",
    "secondary": "#6c757d",
    "success": "#28a745"
  },
  "indexedData": [                  // ✓ Use array for indexed collections
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
  ]
}
```

### 6. Documentation Through Structure
```json
{
  "metadata": {
    "version": "1.0.0",
    "created": "2023-12-01T10:30:00Z",
    "description": "User configuration file"
  },
  "configuration": {
    "database": {
      "host": "localhost",
      "port": 5432,
      "name": "myapp"
    },
    "features": {
      "enableLogging": true,
      "enableCaching": false,
      "maxRetries": 3
    }
  }
}
```

---

## Validation and Testing

### 1. JSON Validators
- **Online Tools**: JSONLint, JSON Formatter & Validator
- **Command Line**: `jq`, `python -m json.tool`
- **IDE Extensions**: JSON validation plugins

### 2. Validation Commands
```bash
# Using jq to validate JSON
jq . < file.json

# Using Python to validate JSON
python -c "import json; json.load(open('file.json'))"

# Using Node.js to validate JSON
node -e "JSON.parse(require('fs').readFileSync('file.json', 'utf8'))"
```

### 3. Schema Validation
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "minLength": 1
    },
    "age": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": ["name", "age"]
}
```

### 4. Testing Checklist
- [ ] All strings are properly quoted with double quotes
- [ ] All object keys are quoted
- [ ] No trailing commas
- [ ] Proper nesting structure
- [ ] Valid data types for all values
- [ ] No JavaScript-specific syntax (functions, undefined, etc.)
- [ ] Consistent naming conventions
- [ ] Proper escaping of special characters
- [ ] Valid Unicode sequences
- [ ] No circular references

### 5. Error Prevention
1. **Use a JSON-aware editor** with syntax highlighting
2. **Enable JSON validation** in your development environment
3. **Use linting tools** to catch errors early
4. **Test with multiple parsers** to ensure compatibility
5. **Validate against schema** when applicable
6. **Use automated testing** for JSON generation code

---

## Summary

Following these guidelines will ensure your JSON is:
- **Syntactically correct** and parseable by all JSON parsers
- **Readable and maintainable** by developers
- **Consistent** across your project
- **Error-free** and robust

Remember: JSON is stricter than JavaScript object notation. When in doubt, validate your JSON using online tools or command-line validators before using it in production.