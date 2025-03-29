## README.md

# AnyActive: URL Classifier Based on HTTP Codes

A Python tool for checking the status codes of URLs or subdomains and categorizing them into different response groups.  

## Features  
- Check individual URLs or bulk subdomains from a file  
- Categorizes responses into:  
  - **2xx**: Successful responses  
  - **3xx**: Redirection responses  
  - **4xx**: Client error responses  
  - **5xx**: Server error responses  
- Displays detailed response headers in single URL mode  
- Saves results in organized text files  
- Custom output directory support  

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/callmelokzy/anyactive
   cd anyactive
   ```  

2. Install dependencies:  
   ```bash
   pip3 install -r requirements.txt
   ```  

## Usage  
**Check a single URL:**  
```bash
python3 anyactive.py -u "<URL>" [-d "<output_directory>"]
```

**Check multiple subdomains from a file:**  
```bash
python3 anyactive.py -l "<path_to_subdomains_file>" [-d "<output_directory>"]
```

**Example Commands:**  
```bash
python3 anyactive.py -u https://example.com
python3 anyactive.py -l subdomains.txt -d results
```

## Output  
- Results are saved in text files like:  
  - `successful_2xx.txt`  
  - `redirection_3xx.txt`  
  - `clienterror_4xx.txt`  
  - `servererror_5xx.txt`  

If no directory is specified, files are saved in the current working directory.  

## Sample Output Screenshots  
**Single URL Check:**  
![image](https://user-images.githubusercontent.com/56486732/212749669-9b78d2b3-4212-43b0-a590-901090184d55.png)  

**Bulk URL Check:**  
![image](https://user-images.githubusercontent.com/56486732/212759227-c6c132e7-c549-47fa-a757-304306b75bd0.png)  

## Notes  
- The tool includes a timeout of 5 seconds for each request to improve efficiency.  
- Invalid or unreachable domains are skipped without halting the script.  

