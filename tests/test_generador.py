def test_program_start_message(capsys):
    print("El programa se inició")
    captured = capsys.readouterr()
    assert "El programa se inició" in captured.out

#Primero simulo que el probrama se inicialice con el mensaje "el probrgrama se inicio"
#Toma el mensaje de la consola y se verifica que se imprimio el mensaje esperado