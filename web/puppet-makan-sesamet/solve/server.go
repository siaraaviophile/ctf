package main

import "net/http"

func main() {
    server := http.Server{
        Addr:    "0.0.0.0:45000",
        Handler: http.HandlerFunc(index),
    }

    err := server.ListenAndServe()
    if err != nil {
        panic(err)
    }
}

func index(w http.ResponseWriter, r *http.Request) {
    cookie := http.Cookie{
        Name:  "paantuch",
        Value: "SVRDTFVCe2MwMGsxZV9jMDBrMWVfdHJhbGFsYWxhXzM4NDgyfQ==",
    }
    http.SetCookie(w, &cookie)

    w.WriteHeader(http.StatusOK)
    w.Write([]byte("Paantuch"))
}
