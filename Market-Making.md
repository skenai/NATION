# Market Making in NATION Network

## Overview
Market making in the [[NATION Network]] focuses on providing liquidity for [[BOKER]] prediction markets and supporting the [[SHIBAKEN Token]] ecosystem. The system combines poker-style gameplay mechanics with energy-backed stability.

## Core Markets

### SHIBAK-nSPV/AVAX
- **Purpose**: Proposal-specific prediction markets
- **Implementation**: [[BOKER|1-G-L0-230-BOKER]]
- **Contract**: 0xa4cf2afd3b165975afffbf7e487cdd40c894ab6b (SHIBAKEN)
- **Pairs**: Individual markets per proposal

### SHIBAK-nSBR/AVAX
- **Purpose**: Bitcoin reserve accumulation
- **Implementation**: [[BOKER|1-G-L0-230-BOKER]]
- **Stability**: Energy cost correlation
- **Heritage**: Technology and innovation preservation

## Market Maker Tiers

### 1. Founding Members
- **Stake**: 100M [[SHIBAKEN Token]]
- **Lock Period**: 12 months
- **Daily Rewards**: 0.1%
- **Benefits**:
  * Priority order execution
  * Enhanced reward multipliers
  * Governance rights
  * Bitcoin reserve participation

### 2. Market Makers
- **Stake**: 50M [[SHIBAKEN Token]]
- **Lock Period**: 6 months
- **Daily Rewards**: 0.05%
- **Benefits**:
  * Standard order execution
  * Base reward multipliers
  * Limited governance rights

### 3. Liquidity Providers
- **Stake**: 10M [[SHIBAKEN Token]]
- **Lock Period**: 3 months
- **Daily Rewards**: 0.025%
- **Benefits**:
  * Basic liquidity provision
  * Participation rewards

## Market Making Strategies

### 1. Proposal Markets
```python
class ProposalMarketMaker:
    def calculate_spread(self, market_depth: float) -> float:
        """Calculate optimal spread based on market depth"""
        return min(
            BASE_SPREAD * (1 + DEPTH_FACTOR / market_depth),
            MAX_SPREAD
        )

    def position_size(self, volatility: float) -> float:
        """Determine position size based on volatility"""
        return MAX_POSITION * exp(-RISK_FACTOR * volatility)
```

### 2. Reserve Markets
```python
class ReserveMarketMaker:
    def bitcoin_allocation(self, energy_cost: float) -> float:
        """Calculate Bitcoin allocation based on energy costs"""
        return min(
            NETWORK_REVENUE * RESERVE_RATIO,
            energy_cost * ENERGY_FACTOR
        )

    def rebalance_frequency(self, price_volatility: float) -> int:
        """Determine rebalancing frequency"""
        return max(
            MIN_REBALANCE_INTERVAL,
            int(BASE_INTERVAL * price_volatility)
        )
```

## Integration with WILLPOWER

### 1. Market Prediction
- Pattern recognition for proposal outcomes
- Market sentiment analysis
- Risk assessment
- Position optimization

### 2. Energy Cost Validation
- Real-time energy price monitoring
- Cost-basis calculations
- Efficiency metrics
- Network stability assessment

## Risk Management

### 1. Position Limits
```python
def calculate_position_limit(
    market_cap: float,
    daily_volume: float,
    maker_tier: str
) -> float:
    """Calculate maximum position size for market maker"""
    base_limit = min(market_cap * MAX_CAP_RATIO, 
                    daily_volume * MAX_VOLUME_RATIO)
    
    tier_multipliers = {
        'founding': 1.0,
        'maker': 0.5,
        'provider': 0.25
    }
    
    return base_limit * tier_multipliers[maker_tier]
```

### 2. Spread Requirements
```python
def minimum_spread(
    volatility: float,
    market_depth: float,
    maker_tier: str
) -> float:
    """Calculate minimum spread requirement"""
    base_spread = MAX_SPREAD * (volatility / MAX_VOLATILITY)
    depth_adjustment = 1 - (market_depth / MAX_DEPTH)
    
    tier_discounts = {
        'founding': 0.5,
        'maker': 0.75,
        'provider': 1.0
    }
    
    return base_spread * (1 + depth_adjustment) * tier_discounts[maker_tier]
```

## Performance Metrics

### 1. Market Making Quality
- Spread maintenance
- Market depth
- Price stability
- Order book balance

### 2. Risk Metrics
- Value at Risk (VaR)
- Expected Shortfall
- Liquidity Risk
- Counterparty Exposure

## Reward Distribution

### 1. Base Rewards
- Daily staking rewards
- Market making fees
- Proposal outcome bonuses
- Bitcoin reserve participation

### 2. Performance Multipliers
- Spread tightness bonus
- Depth contribution
- Uptime rewards
- Stability maintenance

## Related Pages
- [[BOKER]]
- [[SHIBAKEN Token]]
- [[Token System]]
- [[Bitcoin Strategy]]
- [[WILLPOWER]]
