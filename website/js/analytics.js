// SHIBAKEN Token Analytics
const SHIBAKEN_ADDRESS = '0xa4cf2afd3b165975afffbf7e487cdd40c894ab6b';
const NETWORK_SEATS = 100;

// ABI for basic token info
const TOKEN_ABI = [
    {
        "constant": true,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    }
];

// Initialize Web3 and contract
async function initWeb3() {
    if (window.ethereum) {
        window.web3 = new Web3(window.ethereum);
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            return true;
        } catch (error) {
            console.error("User denied account access");
            return false;
        }
    } else if (window.web3) {
        window.web3 = new Web3(window.web3.currentProvider);
        return true;
    } else {
        console.log('No Web3 detected');
        return false;
    }
}

// Format large numbers
function formatNumber(num) {
    if (num >= 1e15) return (num / 1e15).toFixed(2) + ' Quadrillion';
    if (num >= 1e12) return (num / 1e12).toFixed(2) + ' Trillion';
    if (num >= 1e9) return (num / 1e9).toFixed(2) + ' Billion';
    if (num >= 1e6) return (num / 1e6).toFixed(2) + ' Million';
    return num.toLocaleString();
}

// Update metrics display
async function updateMetrics() {
    const contract = new web3.eth.Contract(TOKEN_ABI, SHIBAKEN_ADDRESS);
    
    try {
        // Get circulating supply
        const totalSupply = await contract.methods.totalSupply().call();
        document.getElementById('circulatingSupply').textContent = 
            formatNumber(web3.utils.fromWei(totalSupply, 'ether'));

        // Get holder count from Etherscan API
        const response = await fetch(`https://api.etherscan.io/api?module=token&action=tokenholderlist&contractaddress=${SHIBAKEN_ADDRESS}`);
        const data = await response.json();
        if (data.status === '1') {
            document.getElementById('holders').textContent = formatNumber(data.result.length);
        }

        // Calculate network seats filled
        const seatRequirement = web3.utils.toWei('100000000', 'ether'); // 100M SHIBAKEN
        let seatsCount = 0;
        for (const holder of data.result) {
            if (web3.utils.toBN(holder.TokenHolderQuantity).gte(web3.utils.toBN(seatRequirement))) {
                seatsCount++;
            }
            if (seatsCount >= NETWORK_SEATS) break;
        }
        document.getElementById('networkSeats').textContent = `${seatsCount}/${NETWORK_SEATS}`;

    } catch (error) {
        console.error('Error fetching metrics:', error);
    }
}

// Initialize analytics
async function initAnalytics() {
    const web3Available = await initWeb3();
    if (web3Available) {
        updateMetrics();
        // Update metrics every 5 minutes
        setInterval(updateMetrics, 300000);
    } else {
        document.getElementById('circulatingSupply').textContent = 'Web3 not available';
        document.getElementById('holders').textContent = 'Web3 not available';
        document.getElementById('networkSeats').textContent = 'Web3 not available';
    }
}

// Start analytics when page loads
window.addEventListener('load', initAnalytics);
