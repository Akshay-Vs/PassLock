#include <cstdint>
#include <iostream>
#include <fstream>
#include <cstring>
#include "python.h"


#ifdef fullDebug
    bool debugPcapGlobalHeader = true;
    bool debugPcapPacketHeader = true;
    bool debugEthernetHeader = true;
    bool debugIpHeader = true;
    bool debugTcpUdpHeader = true;
    bool debugInfo = true;
    bool debugPacket = true;
#else
    bool debugPcapGlobalHeader = false;
    bool debugPcapPacketHeader = false;
    bool debugEthernetHeader = false;
    bool debugIpHeader = false;
    bool debugTcpUdpHeader = false;
    bool debugInfo = false;
    bool debugPacket = false;
#endif
    bool debugFilteredPacket = false;
    bool debugFilteredPacketVec = true;
    bool debugFinalData = false;
       ifstream pcapFile;
    pcapFile.open(inputFile.c_str(),  ios::binary);

    if(!pcapFile.is_open()) {
    cerr << "Failed To Open file" << endl;
    return 0;
    } else {
    if(debugInfo)
    cout << "file opened SuccessFully" << std::endl;
    }

    if(debugInfo)
    cout << "buffer[]" << endl;
    pcapFile.seekg(0, pcapFile.end);
    long sizeOfPcap = pcapFile.tellg();
    pcapFile.seekg(0, pcapFile.beg);

    if(debugInfo)
    cout << "File Size: " << sizeOfPcap << endl;
    	int pcapPointer = 0;
    	int pcapPointerStart = 0;
    char * buffer;
    buffer = new char [sizeOfPcap];
    	streamsize loadBites = pcapFile.readsome(buffer, sizeOfPcap);
    if(debugInfo) {
	    cout << "Pointer " << decAndHexStr(pcapPointer) << endl;
    	cout << "PointerStart: " << decAndHexStr(pcapPointerStart) << endl;
    cout << "transferDataSizeByte: " << decAndHexStr(transferDataSizeByte) << endl;
    cout << "pcapPointerStart + transferDataSizeByte: " << decAndHexStr(pcapPointerStart + transferDataSizeByte) << endl;
    }
    if(loadBites != sizeOfPcap) {
        cerr << "expected: " << sizeOfPcap << "  stored: " << loadBites << endl;
        cerr.flush();
        return 0;
    } else {
        if(debugInfo)
            cout << "File Loaded Successfully " << std::endl;
    }
