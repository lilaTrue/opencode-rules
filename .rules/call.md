# JSON Call Guidelines

## Overview
This document provides essential guidelines for AI assistants when working with JSON to prevent and handle common parsing errors, particularly the "JSON Parse error: Expected '}'" error.

## Core Principles

### 1. Always Validate Before Processing
- **NEVER** directly process JSON without validation
- **ALWAYS** validate JSON syntax before any operation
- Use proper JSON validation methods to catch errors early

### 2. Prevention is Better Than Correction
- Structure JSON calls methodically
- Use proper formatting and indentation
- Verify bracket and brace matching before execution

## Common JSON Parse Errors

### Primary Error Pattern
```
JSON Parse error: Expected '}'
JSON Parse Error end
```

This error typically occurs when:
- Missing closing braces `}`
- Missing closing brackets `]`
- Incorrect comma placement
- Unescaped quotes within strings
- Trailing commas in objects or arrays

## Best Practices

### 1. Pre-Validation Workflow
```
1. Construct JSON structure
2. Validate syntax using JSON parser
3. Check for common error patterns
4. Execute the call only after validation passes
```

### 2. Error Recovery Protocol
When encountering "JSON Parse error: Expected '}'" or similar errors:

1. **STOP** the current operation immediately
2. **ANALYZE** the JSON structure for syntax errors
3. **IDENTIFY** the specific issue (missing braces, brackets, commas)
4. **CORRECT** the JSON syntax
5. **RE-VALIDATE** the corrected JSON
6. **RETRY** the call with the corrected JSON

### 3. Systematic JSON Construction
- Start with proper opening braces/brackets
- Add content systematically
- Ensure each opening has a corresponding closing
- Validate at each major structural addition

## Implementation Guidelines

### For AI Assistants
1. **Before any JSON call:**
   - Parse the JSON to verify syntax
   - Check for balanced braces and brackets
   - Validate comma placement
   - Ensure proper string escaping

2. **During JSON construction:**
   - Use consistent indentation
   - Add closing braces/brackets immediately after opening
   - Validate incrementally during construction

3. **Error handling:**
   - Implement automatic retry with correction
   - Log the specific error and correction made
   - Learn from common error patterns

### Validation Checklist
- [ ] All opening braces `{` have matching closing braces `}`
- [ ] All opening brackets `[` have matching closing brackets `]`
- [ ] No trailing commas after last elements
- [ ] All strings are properly quoted and escaped
- [ ] Proper comma separation between elements
- [ ] Valid JSON data types used

## Error Recovery Examples

### Example 1: Missing Closing Brace
**Incorrect:**
```json
{
  "name": "example",
  "value": 123
```

**Corrected:**
```json
{
  "name": "example",
  "value": 123
}
```

### Example 2: Trailing Comma
**Incorrect:**
```json
{
  "name": "example",
  "value": 123,
}
```

**Corrected:**
```json
{
  "name": "example",
  "value": 123
}
```

### Example 3: Unescaped Quotes
**Incorrect:**
```json
{
  "message": "He said "hello" to me"
}
```

**Corrected:**
```json
{
  "message": "He said \"hello\" to me"
}
```

## Mandatory Workflow

### For Every JSON Operation:
1. **Construct** the JSON structure
2. **Validate** using JSON.parse() or equivalent
3. **Handle** any validation errors immediately
4. **Proceed** only with valid JSON
5. **Monitor** for runtime errors and implement recovery

### Error Response Protocol:
1. **Detect** JSON parse error
2. **Analyze** the error message for specific issue
3. **Locate** the problematic section in JSON
4. **Fix** the syntax error
5. **Re-validate** the corrected JSON
6. **Retry** the operation

## Tools and Methods

### Recommended Validation Approaches:
- Use built-in JSON parsers for validation
- Implement bracket/brace counting algorithms
- Use linting tools for JSON syntax checking
- Implement automated error detection and correction

### Testing Strategy:
- Test with malformed JSON examples
- Verify error recovery mechanisms
- Ensure robust error handling in all scenarios

## Conclusion

Following these guidelines will significantly reduce JSON parsing errors and ensure robust error recovery when issues do occur. The key is to always validate before processing and implement systematic error recovery procedures.

**Remember: Prevention through validation is always better than correction after errors occur.**