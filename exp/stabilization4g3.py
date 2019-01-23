#!/usr/bin/env python
import sys
import os
import subprocess
import traceback
import pdb
from bdb import BdbQuit
subprocess.Popen('find ./exp/.. -iname "*.pyc" -delete'.split())
sys.path.insert(0, '.')
os.nice(19)
from main import main
name = __file__.split('/')[-1].split('.')[0]  # name is filename

args = [
    '--name', name,
    '--dataset', 'charades_video',
    '--print-freq', '1',
    '--arch', 'resnet50_3d_autoencoder',
    '--wrapper', 'default',
    '--tasks', 'stabilization_autoencoder_task',
    '--train-file', '/nfs.yoda/gsigurds/CharadesEgo_v1_train.csv',
    '--val-file', '/nfs.yoda/gsigurds/CharadesEgo_v1_test.csv',
    '--data', '/scratch/gsigurds/CharadesEgo_v1_rgb/',
    '--pretrained',
    '--resume', '/nfs.yoda/gsigurds/caches/autoencoder1b/model.pth.tar',
    '--lr', '1e-2',
    #'--lr', '0.005',
    '--weight-decay', '0',
    '--batch-size', '1',
    '--val-size', '0',
    '--cache-dir', '/nfs.yoda/gsigurds/caches/',
    '--epochs', '1000',
    '--workers', '0',
    '--evaluate',
    '--features', 'conv1;layer1;layer4;fc',
    '--content-weight', '10000',
    '--motion-weight', '1',
    '--stabilization-target', 'autoencoder3',
    '--style-weight', '0',
    '--grid-weight', '0',
]
sys.argv.extend(args)
try:
    main()
except BdbQuit:
    sys.exit(1)
except Exception:
    traceback.print_exc()
    print('')
    pdb.post_mortem()
    sys.exit(1)