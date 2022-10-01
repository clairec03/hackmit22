export default function Video({ src }) {
    return (
        <video controls>
            <source src={src} type="video/mp4" />
            Sorry, your browser doesn't support videos.
        </video>
    );
}
