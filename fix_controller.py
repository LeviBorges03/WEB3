with open('/home/jules/WEB3/BibliotecaV2/Controllers/BibliotecaController.cs', 'r') as f:
    content = f.read()

if 'public IActionResult Livro()' not in content:
    # Replace the last closing brace with the new methods
    content = content.rstrip()
    if content.endswith('}'):
        content = content[:-1] + '''
    public IActionResult Livro()
    {
        return View();
    }

    public IActionResult Autor()
    {
        return View();
    }
}
'''
        with open('/home/jules/WEB3/BibliotecaV2/Controllers/BibliotecaController.cs', 'w') as f:
            f.write(content)
        print("Updated successfully")
    else:
        print("Unexpected end of file")
else:
    print("Methods already exist")
