# SKENAI XP/Proposal Event System Implementation

## Table of Contents
- [1. Additional Event Types & XP Values](#1-additional-event-types--xp-values)
- [2. Database & Flow Patterns](#2-database--flow-patterns)
- [3. System Mechanics](#3-system-mechanics)
- [4. Edge Cases & Scaling](#4-edge-cases--scaling)

## 1. Additional Event Types & XP Values

### User Actions (Beyond Basics)
* `PROFILE_COMPLETION_ADVANCED`: Completing non-essential profile sections (15 XP)
* `FEATURE_ADOPTION_FIRST_USE`: First use of new platform features (25 XP per feature)
* `CONTENT_UPVOTE_RECEIVED`: Upvotes on comments/proposals (1-2 XP, daily cap)
* `CONTENT_DOWNVOTE_RECEIVED`: Optional negative XP for consistent downvotes (-1 XP)
* `BUG_REPORT_ACCEPTED`: Verified bug reports (50-100 XP by severity)
* `DOCUMENTATION_CONTRIBUTION_ACCEPTED`: Merged documentation contributions (75-150 XP)
* `USER_REFERRAL_SUCCESSFUL`: New user completes onboarding via referral (100 XP)
* `SOCIAL_SHARE_COMPLETED`: Platform sharing on social media (10 XP, daily cap)

### Proposal Quality/Speed Bonuses
* `PROPOSAL_EARLY_SUBMISSION`: Early submissions (+10% base XP)
* `PROPOSAL_QUALITY_SCORE_HIGH`: High validator ratings (+15-25% base XP)
* `PROPOSAL_ACCEPTED_FIRST_ROUND`: No major revisions needed (50 XP)
* `PROPOSAL_INCLUDES_DETAILED_METRICS`: Clear success metrics included (20 XP)

### Team Achievements
* `TEAM_FIRST_PROPOSAL_SUBMITTED`: Team's first proposal (50 XP per member)
* `TEAM_PROPOSAL_ACCEPTED`: Team proposal acceptance (100 XP per member)
* `TEAM_COMPLETES_CHALLENGE`: Challenge completion (varies by difficulty)
* `TEAM_CONSISTENT_VELOCITY`: Sustained proposal activity (200 XP quarterly)

### Governance Participation
* `GOVERNANCE_VOTE_CAST`: Voting participation (10 XP per vote)
* `GOVERNANCE_PROPOSAL_SUBMITTED`: Governance change proposals (150 XP)
* `GOVERNANCE_DELEGATION_RECEIVED`: Receiving vote delegation (5 XP, capped)
* `GOVERNANCE_FORUM_PARTICIPATION`: Quality forum contributions (5-10 XP)

### Validator/Reviewer Incentives
* `VALIDATION_COMPLETED_ON_TIME`: Timely reviews (25 XP)
* `VALIDATION_ACCURACY_CONFIRMED`: Accurate validation decisions (30 XP)
* `VALIDATION_DETAILED_FEEDBACK`: Exceptional feedback quality (20 XP)
* `VALIDATION_DISPUTE_RESOLUTION`: Dispute resolution help (40 XP)
* `VALIDATION_QUEUE_CONTRIBUTION`: Consistent reviewing (75 XP weekly)

### Special Events & Comments
* Event XP Multipliers: 1.5x-2x during special events
* `COMMENT_MARKED_HELPFUL`: Helpful comment recognition (15 XP)
* `COMMENT_RECEIVED_UPVOTES`: Comment quality indicator (1 XP per upvote)
* `COMMENT_SPARKED_DISCUSSION`: Generating constructive discussion (25 XP)

## 2. Database & Flow Patterns

### DynamoDB Schema (Single-Table Design)
```
Core Entities: USER, PROPOSAL, COMMENT, VALIDATION, EVENT, TEAM, ACHIEVEMENT

User Data:
PK: USER#<UserID>, SK: PROFILE
PK: USER#<UserID>, SK: XP_TOTAL
PK: USER#<UserID>, SK: EVENT#<TimestampISO>#<EventID>
PK: USER#<UserID>, SK: ACHIEVEMENT#<AchievementID>
PK: USER#<UserID>, SK: TEAM#<TeamID>

Proposal Data:
PK: PROPOSAL#<ProposalID>, SK: METADATA
PK: PROPOSAL#<ProposalID>, SK: VERSION#<TimestampISO>
PK: PROPOSAL#<ProposalID>, SK: COMMENT#<TimestampISO>#<CommentID>
PK: PROPOSAL#<ProposalID>, SK: VALIDATION#<ValidatorID>#<TimestampISO>
PK: PROPOSAL#<ProposalID>, SK: EVENT#<TimestampISO>#<EventID>

Team Data:
PK: TEAM#<TeamID>, SK: METADATA
PK: TEAM#<TeamID>, SK: MEMBER#<UserID>
PK: TEAM#<TeamID>, SK: PROPOSAL#<ProposalID>
```

### Global Secondary Indexes (GSIs)
1. XP Leaderboard: GSI1 (PK: XP_LEADERBOARD, SK: XP_TOTAL#<UserID>)
2. Proposal Status: GSI2 (PK: PROPOSAL_STATUS, SK: LAST_UPDATED_TIMESTAMP#<ProposalID>)
3. User Proposals: GSI3 (PK: USER#<UserID>, SK: PROPOSAL#<ProposalID>)
4. Comment Threading: GSI4 (PK: PROPOSAL#<ProposalID>#COMMENT#<ParentCommentID>)
5. Validator History: GSI5 (PK: VALIDATOR#<UserID>, SK: TIMESTAMP#<ProposalID>)
6. Proposal Validations: GSI6 (PK: PROPOSAL#<ProposalID>, SK: VALIDATION#<TimestampISO>)

### Event Flow Architecture
```
Next.js UI
   ↓
API Layer (Auth, Validation)
   ↓
Redpanda Topics
   ↓
Lambda Consumers
   ↓
DynamoDB + Cache Layer
```

## 3. System Mechanics

### XP Management
- Corrections via `XP_CORRECTION` events
- Atomic counters for XP updates
- Achievement tracking and unlocks
- Leaderboard maintenance (near real-time or batch)

### Proposal System
- Version control with timestamps
- Status tracking and transitions
- Validation queue management
- Comment threading and moderation

### GFORCE Integration
- XP-based voting weight calculation
- Delegation tracking
- Proposal impact measurement

## 4. Edge Cases & Scaling

### High-Volume Handling
- Redpanda partition strategy
- Lambda concurrency management
- DynamoDB capacity planning
- Cache layer optimization

### Data Consistency
- Idempotent event processing
- Conditional updates
- Transaction boundaries
- Cache invalidation strategies

### Performance Optimization
- Query patterns optimization
- Index utilization
- Cache strategies
- Monitoring and alerting setup

### System Resilience
- Error handling
- Maintenance procedures
- Dispute resolution
- Data recovery processes
