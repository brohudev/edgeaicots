# Log

### 4/25 
- successfully flashed micropython onto the board. 
- moving onto the pi. 

### 5/2
- Ran int8 MLP fault injector: 100 samples, 8-16-5, rates 0..5e-3
- Result: zero accuracy degradation at tested rates (model too small/redundant for low SEU rates)
- Inference latency: ~196ms per rate point on 240MHz ESP32-S3
- File: seu_baseline_esp32.txt saved to device flash and pulled to repo
- BLOCKED: Pi 4 not booting (ssh over usb issue to fix)
- NEXT: Run higher flip rates to find degradation knee; fix Pi or order 2nd ESP32 for lockstep