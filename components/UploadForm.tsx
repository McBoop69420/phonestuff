'use client';

import { useState, useRef } from 'react';
import type { Bet } from '@/lib/db';

interface Props {
  onBetAdded: (bet: Bet) => void;
}

export default function UploadForm({ onBetAdded }: Props) {
  const [state, setState] = useState<'idle' | 'uploading' | 'error'>('idle');
  const [errorMsg, setErrorMsg] = useState('');
  const [preview, setPreview] = useState<string | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  async function handleFile(file: File) {
    setPreview(URL.createObjectURL(file));
    setState('uploading');
    setErrorMsg('');

    const form = new FormData();
    form.append('image', file);

    try {
      const res = await fetch('/api/bets', { method: 'POST', body: form });
      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.error || 'Upload failed');
      }
      onBetAdded(data as Bet);
      setState('idle');
      setPreview(null);
      if (inputRef.current) inputRef.current.value = '';
    } catch (e) {
      setState('error');
      setErrorMsg(e instanceof Error ? e.message : 'Unknown error');
    }
  }

  function onInputChange(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    if (file) handleFile(file);
  }

  function onDrop(e: React.DragEvent) {
    e.preventDefault();
    const file = e.dataTransfer.files?.[0];
    if (file) handleFile(file);
  }

  return (
    <div
      onDrop={onDrop}
      onDragOver={(e) => e.preventDefault()}
      className="rounded-xl border-2 border-dashed border-gray-600 hover:border-blue-500 transition-colors p-6 text-center cursor-pointer"
      onClick={() => inputRef.current?.click()}
    >
      <input
        ref={inputRef}
        type="file"
        accept="image/*"
        className="hidden"
        onChange={onInputChange}
      />

      {state === 'uploading' ? (
        <div className="flex flex-col items-center gap-3">
          {preview && <img src={preview} alt="Bet slip preview" className="max-h-32 rounded-lg object-contain opacity-60" />}
          <div className="flex items-center gap-2 text-blue-400">
            <svg className="animate-spin w-5 h-5" viewBox="0 0 24 24" fill="none">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z" />
            </svg>
            <span className="text-sm">Reading your bet slip...</span>
          </div>
        </div>
      ) : (
        <div className="flex flex-col items-center gap-2 text-gray-400">
          <svg className="w-10 h-10 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5" />
          </svg>
          <p className="text-sm font-medium text-gray-300">Upload bet slip photo</p>
          <p className="text-xs text-gray-500">Tap or drag & drop · JPG, PNG, WEBP</p>
        </div>
      )}

      {state === 'error' && (
        <p className="mt-3 text-sm text-red-400">{errorMsg}</p>
      )}
    </div>
  );
}
