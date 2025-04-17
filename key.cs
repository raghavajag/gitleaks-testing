public class SecurityConfig {
    const string privateKey = 
    @"-----BEGIN ENCRYPTED PRIVATE KEY-----
    MIIFDjBABgkqhkiG9w0BBQ0wMzAbBgkqhkiG9w0BBQwwDgQItC8yQMKngtICAggA
    MBQGCCqGSIb3DQMHBAhA7gVqsINvJg==
    -----END ENCRYPTED PRIVATE KEY-----";
}
const string certChain = 
@"-----BEGIN CERTIFICATE-----
MIIFazCCA1OgAwIBAgIUTp3gI1oTDXKgHf3m/6xBlUzowNcwDQYJKoZIhvcNAQEL
-----END CERTIFICATE-----
-----BEGIN EC PRIVATE KEY-----
MHcCAQEEIKrmW4lJB1RgC3vFw9sx3p+QbJb1ns75AIITk9kUXkOcoAoGCCqGSM49
-----END EC PRIVATE KEY-----";



/* 
 * Security configuration:
 */
const string legacyKey =
    "-----BEGIN RSA PRIVATE KEY-----\n" +
    "Proc-Type: 4,ENCRYPTED\n" +
    "DEK-Info: AES-256-CBC,2E354B33C84121CBC155B712\n" +
    "MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgWvJsz6WpZQbJfR5F\n" +
    "-----END RSA PRIVATE KEY-----";

// Missing end tag
string partialKey = 
@"-----BEGIN DSA PRIVATE KEY-----
MIIBuwIBAAKBgQDl4dYE8GpXgQANp0jP7QN5w7QJqy4GjZvZ7W8WJ1x4K7t
// Oops forgot to close the PEM block";
