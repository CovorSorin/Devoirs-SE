"""
Le premier prgramme en Python
* utilisation des arguments de la lignne de commande
* les listes et la fonction map
* les threads
* le logger

@author Dragos STOICA
@version 0.4
@date 16.feb.2014
"""
import time
import random
import logging
import sys, threading, logging, os
import multiprocessing
from multiprocessing import Process, Queue, current_process, freeze_support
from threading import Thread
from time import sleep


class Bonjour(threading.Thread):
    def __init__(self, personne):
        threading.Thread.__init__(self)
        self.personne = personne
    def run(self):
        #Fonction polie - saluer une personne
        print "Bonjour %(personne)s!\n" % \
          {"personne":self.personne},
        logging.info("Bonjour : %(personne)s" %{"personne":self.personne})

def worker(input, output):
    for func, args in iter(input.get, 'STOP'):
        result = execute_function(func, args)
        output.put(result)

def utilisation():
    #Affichage mode d'utilisation
    print """
          Le programme doit etre appelle avec minimum 1 argument:
          python bonjour_listes.py Dragos
          """

def execute_function(func, args):
    result = func(args)
    return '%s says that %s %s = %s' % \
        (threading.current_thread().name, func.__name__, args, result)

def main(argv=None):
    working_dir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
    #Configurez le logging pour ecrire dans un fichier texte
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        filename=working_dir + 'process.log',
                        level=logging.INFO)
    logging.info("Main start")

    #multiprocessing.log_to_stderr(logging.INFO)

    #La boucle principale
    if argv is None:
        argv = sys.argv

    if len(argv) == 1:
        utilisation()
        return 0
    NUMBER_OF_THREADS = 4
    TASKS1 = []
    TASKS2 = []
    TASKS3 = []

    # Create queues
    task_queue = Queue()
    done_queue = Queue()
    
    with open(working_dir+argv[1], 'r') as f:
    #Dites bonjour a chaque personne de fichier
        for ligne in f:
           if ligne[0:2] == "M.":
               TASKS3.append((Bonjour, (ligne.strip(' \r\n'))))
           if ligne[0:4] == "Mme.":
               TASKS2.append((Bonjour, (ligne.strip(' \r\n'))))
           if ligne[0:5] == "Mlle.":
               TASKS1.append((Bonjour, (ligne.strip(' \r\n'))))
           #logging.info("Ligne: %s" % (ligne.strip(' \r\n')))

    #TASKS1

    # Submit tasks
    for task in TASKS1:
        logging.info(task)
        task_queue.put(task)

    # Start worker processes
    for i in range(NUMBER_OF_THREADS):
        Thread(target=worker, args=(task_queue, done_queue)).start()

    # Get and print results
    for i in range(len(TASKS1)):
        logging.info(done_queue.get())

    #TASKS2

    for task in TASKS2:
        logging.info(task)
        task_queue.put(task)

    # Get and print results
    for i in range(len(TASKS2)):
        logging.info(done_queue.get())

    #TASK3

    # Add more tasks using `put()`
    for task in TASKS3:
        logging.info(task)
        task_queue.put(task)

    # Get and print some more results
    for i in range(len(TASKS3)):
        logging.info(done_queue.get())

    # Tell child processes to stop
    for i in range(NUMBER_OF_THREADS):
        task_queue.put('STOP')
        
    logging.info("Main stop")
    return 0

if __name__ == "__main__":
    #Simplifiez la logique de la fonction principale
    sys.exit(main())
