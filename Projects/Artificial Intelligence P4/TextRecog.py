import os
import time
from Vision import VNImageRequestHandler, VNRecognizeTextRequest, VNRequestTextRecognitionLevelAccurate
from Cocoa import NSURL

class NativeMacOCRExtractor:
    def __init__(self, languages=['en', 'es']):
        """Initializes the native macOS Vision OCR Engine."""
        print("[+] Initializing Apple Native Vision OCR Engine...")
        self.languages = languages
        self.supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp')

    def analyze_image(self, image_path):
        """Performs OCR using Apple's native structural Vision Framework."""
        if not os.path.exists(image_path):
            print(f"[-] Error: File not found at '{image_path}'")
            return None

        start_time = time.time()
        try:
            # Convert text string pathway to a native macOS URL object
            image_url = NSURL.fileURLWithPath_(image_path)
            
            extracted_text = []
            confidences = []

            # Set up the native completion callback handler for processing tracking matrices
            def completion_handler(request, error):
                if error:
                    return
                results = request.results()
                for observation in results:
                    # Grab the top text candidate score matching constraints
                    candidate = observation.topCandidates_(1)[0]
                    extracted_text.append(candidate.string())
                    confidences.append(candidate.confidence() * 100)

            # Create and configure the native core text recognition parameters
            request = VNRecognizeTextRequest.alloc().initWithCompletionHandler_(completion_handler)
            request.setRecognitionLevel_(VNRequestTextRecognitionLevelAccurate)
            request.setRecognitionLanguages_(self.languages)
            request.setUsesLanguageCorrection_(True)

            # Execute the request handler synchronously against the image target
            handler = VNImageRequestHandler.alloc().initWithURL_options_(image_url, None)
            handler.performRequests_error_([request], None)

            full_text = "\n".join(extracted_text).strip()
            avg_confidence = round(sum(confidences) / len(confidences), 2) if confidences else 0.0

            return {
                "text": full_text,
                "confidence": avg_confidence,
                "runtime": round(time.time() - start_time, 2),
                "word_count": len(full_text.split())
            }
        except Exception as e:
            print(f"[-] Failed processing {os.path.basename(image_path)}. Reason: {e}")
            return None

    def export_report(self, image_path, metrics, output_dir):
        """Saves a structured analytical text report summary file securely."""
        os.makedirs(output_dir, exist_ok=True)
        file_name = os.path.splitext(os.path.basename(image_path))[0]
        destination = os.path.join(output_dir, f"{file_name}_ocr_summary.txt")

        with open(destination, "w", encoding="utf-8") as report:
            report.write("========================================\n")
            report.write("    APPLE NATIVE OCR EXTRACTION REPORT   \n")
            report.write("========================================\n")
            report.write(f"Source File    : {os.path.basename(image_path)}\n")
            report.write(f"Confidence     : {metrics['confidence']}%\n")
            report.write(f"Word Count     : {metrics['word_count']}\n")
            report.write(f"Execution Time : {metrics['runtime']} seconds\n")
            report.write("----------------------------------------\n\n")
            report.write(metrics["text"] if metrics["text"] else "[No readable text found]")

        print(f"[+] Diagnostic report written safely to: {destination}")

    def run_single(self, image_path, output_dir=None):
        """Pipeline entry point for evaluating a single standalone target file."""
        if output_dir is None:
            # FIX: Isolates file saving relative to image workspace instead of Mac system root
            output_dir = os.path.join(os.path.dirname(image_path), "ocr_results")

        metrics = self.analyze_image(image_path)
        if not metrics:
            return

        print("\n--- Live Text Extraction Preview ---")
        print(metrics["text"] if metrics["text"] else "[Empty text canvas]")
        print("------------------------------------")
        print(f"Metrics -> Confidence: {metrics['confidence']}% | Words: {metrics['word_count']} | Time: {metrics['runtime']}s")
        
        self.export_report(image_path, metrics, output_dir)

    def run_batch(self, directory_path):
        """Scans an entire target path directory and pipelines image loops cleanly."""
        if not os.path.isdir(directory_path):
            print(f"[-] Error: '{directory_path}' is not a valid directory.")
            return

        targets = [f for f in os.listdir(directory_path) if f.lower().endswith(self.supported_formats)]
        if not targets:
            print("[-] No supported image files found inside the targeted folder.")
            return

        print(f"[+] Batch execution initialization: Found {len(targets)} files.")
        batch_output_dir = os.path.join(directory_path, "ocr_results")

        for index, item in enumerate(targets, 1):
            full_path = os.path.join(directory_path, item)
            print(f"\n[{index}/{len(targets)}] Processing target file...")
            metrics = self.analyze_image(full_path)
            if metrics:
                self.export_report(full_path, metrics, batch_output_dir)

        print(f"\n[+] Batch task finished successfully! Results isolated to: {batch_output_dir}")


# --- Terminal Interface Driver ---
if __name__ == "__main__":
    extractor = NativeMacOCRExtractor(languages=['en', 'es'])

    print("=============================================")
    print("      APPLE NATIVE VISION OCR INTERFACE      ")
    print("=============================================")
    print("1 -> Extract text from a single image")
    print("2 -> Batch process a folder full of images")
    
    user_selection = input("\nSelect processing pattern (1 or 2): ").strip()

    if user_selection == "1":
        target_file = input("Enter exact path to target image: ").strip()
        # FIX: Slices away double quotes or formatting quotes added via terminal drag-and-drop structures
        target_file = target_file.strip("'\"")
        extractor.run_single(target_file)
        
    elif user_selection == "2":
        target_folder = input("Enter path to target folder: ").strip()
        target_folder = target_folder.strip("'\"")
        extractor.run_batch(target_folder)
        
    else:
        print("[-] Invalid input token context. Closing engine workflow.")