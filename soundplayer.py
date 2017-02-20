import multiprocessing
from time import time, sleep
from pyglet import media

def __playSoundFile(fileName, loop):
    staticSource = media.load(fileName, streaming=False)
    duration = staticSource.duration

    while True:
        player = staticSource.play()

        startTime = time()
        endTime = startTime + duration
        while time() < endTime:
            sleep(0.1)

        if not loop:
            break
    #print 'Finished playing:', fileName

def playSoundfile(fileName, loop=False):
    audioProcess = multiprocessing.Process(target=__playSoundFile, args=(fileName,loop))
    audioProcess.start()
    #print 'Started playing:', fileName
    return audioProcess

def stopSoundFile(audioProcess):
    if audioProcess:
        audioProcess.terminate()
        audioProcess.join()
    else:
        print 'Invalid audio process, could not stop playback'
