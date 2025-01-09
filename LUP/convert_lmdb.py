#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-12-27 01:08:30
# @Author  : Dengpan Fu (fdpan@mail.ustc.edu.cn)

import os
import numpy as np
import cv2
import lmdb
import pickle

# Directory paths
base_dir = 'luperson'
lmdb_dir = 'lup_lmdb'

# Initialize LMDB environment
keys = []
env = lmdb.open(lmdb_dir, map_size=100 * 1024**3)
txn = env.begin(write=True)
cnt = 0

# Iterate through countries and cities
countries = sorted(os.listdir(base_dir))
for i, country in enumerate(countries):
    country_dir = os.path.join(base_dir, country)
    if not os.path.isdir(country_dir):
        continue
    
    cities = sorted(os.listdir(country_dir))
    for j, city in enumerate(cities):
        city_dir = os.path.join(country_dir, city)
        if not os.path.isdir(city_dir):
            continue
        
        key_prefix = '{:02d}_{:02d}'.format(i, j)
        images = sorted([x for x in os.listdir(city_dir) if x.endswith('.jpg')])
        
        for m, img_name in enumerate(images):
            if cnt % 2000 == 0:
                print('[{:3d}|{:3d}] country={:s}, [{:d}|{:d}] city={:s}, [{:d}|{:d}] image={:s}'.format(
                    i, len(countries), country, j, len(cities), city, m, len(images), img_name))
            
            key_main = '{:08d}'.format(cnt)
            key = key_prefix + '_' + key_main
            img_path = os.path.join(city_dir, img_name)
            
            with open(img_path, 'rb') as f:
                im_str = f.read()
            
            im = np.frombuffer(im_str, np.uint8)
            keys.append(key)
            key_byte = key.encode('ascii')
            txn.put(key_byte, im)
            cnt += 1
        
        # Commit the transaction after processing each city
        txn.commit()
        txn = env.begin(write=True)

# Final commit and close
txn.commit()
env.close()

# Save keys
with open('keys.pkl', 'wb') as f:
    pickle.dump(keys, f)
