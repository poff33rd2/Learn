import React from "react";
import Link from "next/link";
import Image from "next/image";

export default function Navbar() {
    return (
        <nav className="flex items-center bg-white p-4">
            <Image src='/public/HE-red-logo.png' alt='' width={50} height={50}></Image>
            <p className="text-black">OFF 33RD</p>
        </nav>
        
    )
}