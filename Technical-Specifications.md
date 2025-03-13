# Technical Specifications

## Smart Contracts

### EdgeEvolution
- Scale Factor: 1000 (3 decimals)
- Max Edge Strength: 1.0
- Initial Edge: 0.9

Challenge Types (weights):
1. TOKEN_METRICS (1.0x): Value validation
2. SECURITY (1.2x): Edge protection
3. EFFICIENCY (1.1x): Pattern optimization
4. NETWORK (1.3x): Graph properties
5. VALIDATION (1.4x): Proof verification
6. FOUNDATION (1.5x): Hash chain verification

### PriceCalculator
- Base Price: $2,500
- Max Stake: 10M SHIBAK
- Max Impact: $500

Price Components:
1. Base: $2,500
2. Staking: `(staked * edgeStrength * basePrice) / (maxStake * maxEdge)`
3. Challenge: Impact up to $500
4. Edge: Direct strength value

## Implementation Timeline

### Week 1 (March 13-18)
- Deploy contracts to Fuji ✓
- Test edge evolution (0.9 → 1.0) ✓
- Verify price calculation ($2,990.90 → $3,001.00) ✓

### Week 2 (March 19-25)
- WILLPOWER Challenge.calculate_xp integration
- FOUNDATION type implementation
- XP scaling validation

### Week 3-4 (March 26-April 12)
- Pre-sale launch
- 100 seats @ $2,500
- 1M SHIBAK stake requirement
- First 10: FOUNDATION access

## Key Metrics
- Initial TVL: $250k → $300k
- Daily transactions: 100
- Monthly XP: 210M
- Network cap: 24,000 positions
