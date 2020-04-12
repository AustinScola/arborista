import ast

def assert_ast_equal(a: ast.AST, b: ast.AST):
    assert type(a) == type(b)
    a_fields = ast.iter_fields(a)
    b_fields = ast.iter_fields(b)
    for (a_field_name, a_field_value), (b_field_name, b_field_value) in zip(a_fields, b_fields):
        assert a_field_name == b_field_name
        assert type(a_field_value) == type(b_field_value)
        if isinstance(a_field_value, ast.AST):
            assert_ast_equal(a_field_value, b_field_value)
        elif isinstance(a_field_value, list):
            for a_item, b_item in zip(a_field_value, b_field_value):
                assert type(a_item) == type(b_item)
                if isinstance(a_item, ast.AST):
                    assert_ast_equal(a_item, b_item)
                else:
                    assert a_item == b_item
        else:
            assert a_field_value == b_field_value
