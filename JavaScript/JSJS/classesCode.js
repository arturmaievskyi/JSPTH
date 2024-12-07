// File: FileOperations.js
const fs = require('fs');
const path = require('path');

// Function to read a file
function readFile(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}

// Function to write to a file
function writeFile(filePath, content) {
  return new Promise((resolve, reject) => {
    fs.writeFile(filePath, content, 'utf8', (err) => {
      if (err) reject(err);
      else resolve('File written successfully.');
    });
  });
}

// Function to append content to a file
function appendToFile(filePath, content) {
  return new Promise((resolve, reject) => {
    fs.appendFile(filePath, content, 'utf8', (err) => {
      if (err) reject(err);
      else resolve('Content appended successfully.');
    });
  });
}

// Function to delete a file
function deleteFile(filePath) {
  return new Promise((resolve, reject) => {
    fs.unlink(filePath, (err) => {
      if (err) reject(err);
      else resolve('File deleted successfully.');
    });
  });
}

// Function to check if a file exists
function fileExists(filePath) {
  return fs.existsSync(filePath); // Synchronous method for quick existence checks
}

// Function to list files in a directory
function listFiles(directoryPath) {
  return new Promise((resolve, reject) => {
    fs.readdir(directoryPath, (err, files) => {
      if (err) reject(err);
      else resolve(files);
    });
  });
}

// Function to get file stats (size, creation time, etc.)
function getFileStats(filePath) {
  return new Promise((resolve, reject) => {
    fs.stat(filePath, (err, stats) => {
      if (err) reject(err);
      else resolve(stats);
    });
  });
}
