# XP System

## Base Components
- Chat contribution: 5,000 XP
- Stake contribution: 5,500 XP
- Total base: 10,500 XP

## Scaling Formula
```python
XP = min(
    raw_xp,
    base * 2,  # 21,000 cap
    max(
        base * network_size/100,      # Linear scale
        50_000 * network_size/24_000  # Original scale
    )
)
```

## Challenge Multipliers
Challenge type weights impact XP gain:
1. TOKEN_METRICS: 1.0x
2. SECURITY: 1.2x
3. EFFICIENCY: 1.1x
4. NETWORK: 1.3x
5. VALIDATION: 1.4x
6. FOUNDATION: 1.5x

## Network Caps
- MVP Phase: 21,000 XP/action
- Phase 3: 105,000 XP/action
- Network size: ≤ 24,000 positions

## Integration Points
- [WILLPOWER](WILLPOWER.md): Pattern recognition for quality scoring
- [Evolution Arena](Evolution-Arena.md): Challenge validation
- [Network Validation](Network-Validation.md): Completeness verification
