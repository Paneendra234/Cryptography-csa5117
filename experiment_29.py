def sha3_capacity_lane_status():
    rate_lanes = 1024 // 64 
    capacity_lanes = (1600 - 1024) // 64  
    return rate_lanes, capacity_lanes

r_lanes, c_lanes = sha3_capacity_lane_status()
print(f" SHA-3: State has {r_lanes} Rate Lanes and {c_lanes} Capacity Lanes.")
